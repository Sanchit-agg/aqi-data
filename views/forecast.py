import requests
import pandas as pd
import streamlit as st
import plotly.express as px
from streamlit_autorefresh import st_autorefresh


page_bg_img = """
<style>
[data-testid="stAppViewContainer"]{
background: linear-gradient(0deg, rgba(34,193,195,0.7090941011235955) 0%, rgba(79,250,76,0.6416783707865168) 100%);
}
</style>
"""
st.markdown(page_bg_img, unsafe_allow_html=True)
st_autorefresh(interval=3600 * 1000)


st.markdown("<h1 style='text-align: center;'>Pollutant Forecast</h1>", unsafe_allow_html=True)
st.divider()

def session_state():
    st.session_state["city_value"] = st.session_state.city


if "city_value" not in st.session_state:
    st.session_state["city_value"] = 'Delhi'

city = st.text_input(label='_',value=st.session_state["city_value"], label_visibility='hidden', key= 'city', on_change=session_state)
if not city:
    st.error('Please enter a valid input', icon="🚨")



@st.cache_data(ttl=3600)
def fetch_and_process_data(city_name):
    API_KEY = st.secrets['API_KEY']
    url = f"http://api.waqi.info/feed/{city_name}/?token={API_KEY}"
    response = requests.get(url)
    data = response.json()


    df_pm10 = pd.json_normalize(data['data']['forecast']['daily']['pm10']).rename(
        columns={'avg': 'pm10_avg', 'min': 'pm10_min', 'max': 'pm10_max'})
    df_pm25 = pd.json_normalize(data['data']['forecast']['daily']['pm25']).rename(
        columns={'avg': 'pm25_avg', 'min': 'pm25_min', 'max': 'pm25_max'})
    df_o3 = pd.json_normalize(data['data']['forecast']['daily']['o3']).rename(
        columns={'avg': 'o3_avg', 'min': 'o3_min', 'max': 'o3_max'})
    df_uvi = pd.json_normalize(data['data']['forecast']['daily']['uvi']).rename(
        columns={'avg': 'uvi_avg', 'min': 'uvi_min', 'max': 'uvi_max'})


    dfs = [df_pm10, df_pm25, df_o3, df_uvi]
    merged_df = pd.concat([df.set_index('day') for df in dfs], axis=1, join='outer').reset_index()

    return merged_df



merged_df = fetch_and_process_data(city)



def chart_plot(pollutants):
    return px.line(data_frame=merged_df, x='day', y=pollutants, height=400, markers=True)



pollutants = {
    'PM 10': ['pm10_max', 'pm10_avg', 'pm10_min'],
    'PM 2.5': ['pm25_max', 'pm25_avg', 'pm25_min'],
    'O3': ['o3_max', 'o3_avg', 'o3_min'],
    'UV Index': ['uvi_max', 'uvi_avg', 'uvi_min'],
    'Reset': ['pm10_max', 'pm10_avg', 'pm10_min', 'pm25_max', 'pm25_avg', 'pm25_min', 'o3_max', 'o3_avg', 'o3_min',
              'uvi_max', 'uvi_avg', 'uvi_min']
}


col1, col2, col3, col4, col5 = st.columns(5)
buttons = [col1.button('PM 10', use_container_width=True), col2.button('PM 2.5', use_container_width=True),
           col3.button('O3', use_container_width=True), col4.button('UV Index', use_container_width=True),
           col5.button('Reset', use_container_width=True)]


clicked_index = next((i for i, clicked in enumerate(buttons) if clicked), -1)
selected_pollutants = list(pollutants.values())[clicked_index] if clicked_index != -1 else pollutants['Reset']


st.plotly_chart(chart_plot(selected_pollutants))
