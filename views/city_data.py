import requests
import pandas as pd
import streamlit as st
import plotly.express as px
from streamlit_autorefresh import st_autorefresh

st_autorefresh(interval=3600 * 1000)
API_KEY = st.secrets['API_KEY']

# Background color theme
page_bg_img = """
<style>
[data-testid="stAppViewContainer"]{
background: linear-gradient(0deg, rgba(34,193,195,0.7090941011235955) 0%, rgba(79,250,76,0.6416783707865168) 100%);
}
</style>
"""

st.markdown(page_bg_img, unsafe_allow_html=True)

# Page Title
st.markdown("""
<div>
<h1 style="text-align: center;">Enter your city</h1>
</div>
""", unsafe_allow_html=True)


# Getting city name and storing it in streamlit session ('cache')
def session_state():
    st.session_state["city_value"] = st.session_state.city


if "city_value" not in st.session_state:
    st.session_state["city_value"] = 'Delhi'
city = st.text_input(label='_',value=st.session_state["city_value"], label_visibility='hidden', key= 'city', on_change=session_state)

# Caching the data for faster results
@st.cache_data
def city_data(city):
    if city == '':
        st.error('Please enter a valid input', icon="🚨")
    url = f"http://api.waqi.info/feed/{city}/?token={API_KEY}"
    url2 = f'https://api.waqi.info/feed/here/?token={API_KEY}'
    url3 = f'https://api.waqi.info/search/?token={API_KEY}&keyword={city}'
    response = requests.get(url3)
    data = response.json()
    data_object = pd.json_normalize(data)
    normalized_data = pd.json_normalize(data_object['data'])
    normalized_data = normalized_data.transpose()
    data6 = []
    for i in range(len(normalized_data)):
        data4 = pd.DataFrame(normalized_data[0][i])
        data5 = data4.drop(['station.geo'], axis=1)
        data5['station.geo.lat'] = data4['station.geo'][0]
        data5['station.geo.long'] = data4['station.geo'][1]
        data6.append(data5.iloc[0])

    data7 = pd.DataFrame(data=data6)
    # data7['aqi'] = data7['aqi'].replace('-', -1).astype(int)
    data7 = data7.reset_index().drop(['index'], axis=1)
    data7 = data7.drop(data7[data7['aqi'] == '-'].index, axis=0)
    data7['aqi'] = data7['aqi'].astype(int)
    st.dataframe(data7, use_container_width=True)

    def aqi_to_color(aqi):
        # print(aqi)
        if 0 <= aqi <= 50:
            return 'green'  # Good
        elif 51 <= aqi <= 100:
            return 'yellow'  # Moderate
        elif 101 <= aqi <= 150:
            return 'orange'  # Unhealthy for Sensitive Groups
        elif 151 <= aqi <= 200:
            return 'red'  # Unhealthy
        elif 201 <= aqi <= 300:
            return 'purple'  # Very Unhealthy
        elif 301 <= aqi:
            return 'maroon'  # Hazardous
        else:
            return 'gray'  # Invalid AQI


    data7['Color'] = data7['aqi'].apply(aqi_to_color)
    fig = px.scatter_mapbox(data7, lat='station.geo.lat', lon='station.geo.long', zoom=10, height=700,
                             hover_name='station.name',hover_data={'station.geo.lat': False, 'station.geo.long': False,
                                                                   'aqi': True},
        color='Color',  # Use the color column created based on AQI
        color_discrete_map={  # Define color mapping explicitly
            'green': 'green',
            'yellow': 'yellow',
            'orange': 'orange',
            'red': 'red',
            'purple': 'purple',
            'maroon': 'maroon',
            'gray': 'gray'})
    fig.update_layout(showlegend=False)
    fig.update_traces(marker=dict(size=13))
    fig.update_layout(mapbox_style="carto-positron")
    st.plotly_chart(fig)

city_data(st.session_state.city_value)