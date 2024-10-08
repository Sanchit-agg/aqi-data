import requests
import streamlit as st
from streamlit_autorefresh import st_autorefresh


st_autorefresh(interval=3600 * 1000)
API_KEY = st.secrets['API_KEY']


# Function to display Major cities AQI data
@st.cache_data
def api_main():
    # Background color theme
    page_bg_img = """
    <style>
    [data-testid="stAppViewContainer"]{
    background: linear-gradient(0deg, rgba(34,193,195,0.7090941011235955) 0%, rgba(79,250,76,0.6416783707865168) 100%);
    }
    </style>
    """

    st.markdown(page_bg_img, unsafe_allow_html=True)
    # Page title "AQI Data"
    st.markdown(
        """
        <style>
        .centered-title {
            text-align: center;
            font-size: 60px;
            font-weight: bold;
            color: #2C3E50;
        }
        </style>
        <h1 class="centered-title">AQI Data</h1>
        """,
        unsafe_allow_html=True
    )

    st.divider()

    # Function to calculate AQI color and category
    def get_aqi_color(aqi):
        if 0 <= aqi <= 50:
            return '#00E400','Good'  # Green for Good
        elif aqi <= 100:
            return '#FFFF00', 'Moderate'  # Yellow for Moderate
        elif aqi <= 150:
            return '#FF7E00', 'Unhealthy for Sensitive Groups'  # Orange for Unhealthy for Sensitive Groups
        elif aqi <= 200:
            return '#FF0000', 'Unhealthy'  # Red for Unhealthy
        elif aqi <= 300:
            return '#8F3F97', 'Very Unhealthy'  # Purple for Very Unhealthy
        elif 301 <= aqi:
            return '#7E0023', 'Hazardous'  # Maroon for Hazardous
        else:
            return '#BEBEBE'

    # Function ot print city name
    def city_print(city_name):
        st.markdown(f"""
            <div>
            <h2 style="text-align: center;">{city_name}</h2>
            </div>
            """, unsafe_allow_html=True)
    # Function to print AQI category
    def aqi_print(bg_color, bg_text_shadow, aqi_value, aqi_category):
        st.markdown(
            f"""
                <div style="background-color:{bg_color}; padding: 10px; border-radius: 5px;">
                    <h3 style="color:white;{bg_text_shadow} height: 70px; text-align: center;">{aqi_value}
                    \n({aqi_category})</h3>
                </div>
                """, unsafe_allow_html=True
        )

    # Created 6 columns for major 6 cities
    col1, col2, col3, col4, col5, col6 = st.columns(6)
    text_shadow = ''
    with (col1):
        city = 'Delhi'
        city_aqi = requests.get(f"http://api.waqi.info/feed/{city}/?token={API_KEY}").json()['data']['aqi']
        city_print(city)
        color, category = get_aqi_color(city_aqi)
        if color == '#FFFF00':
            text_shadow = 'text-shadow: -0.75px -0.75px 0 black, 0.75px -0.75px 0 black, -0.75px 0.75px 0 black, 0.75px 0.75px 0 black;'
        aqi_print(color, text_shadow, city_aqi, category)
        text_shadow = ''

    with col2:
        city = 'London'
        city_aqi = requests.get(f"http://api.waqi.info/feed/{city}/?token={API_KEY}").json()['data']['aqi']
        city_print(city)
        color, category = get_aqi_color(city_aqi)
        if color == '#FFFF00':
            text_shadow = 'text-shadow: -0.75px -0.75px 0 black, 0.75px -0.75px 0 black, -0.75px 0.75px 0 black, 0.75px 0.75px 0 black;'
        aqi_print(color, text_shadow, city_aqi, category)
        text_shadow = ''

    with col3:
        city = 'New York'
        city_aqi = requests.get(f"http://api.waqi.info/feed/{city}/?token={API_KEY}").json()['data']['aqi']
        city_print(city)
        color, category = get_aqi_color(city_aqi)
        if color == '#FFFF00':
            text_shadow = 'text-shadow: -0.75px -0.75px 0 black, 0.75px -0.75px 0 black, -0.75px 0.75px 0 black, 0.75px 0.75px 0 black;'
        aqi_print(color, text_shadow, city_aqi, category)
        text_shadow = ''

    with col4:
        city = 'Moscow'
        city_aqi = requests.get(f"http://api.waqi.info/feed/{city}/?token={API_KEY}").json()['data']['aqi']
        city_print(city)
        color, category = get_aqi_color(city_aqi)
        if color == '#FFFF00':
            text_shadow = 'text-shadow: -0.75px -0.75px 0 black, 0.75px -0.75px 0 black, -0.75px 0.75px 0 black, 0.75px 0.75px 0 black;'
        aqi_print(color, text_shadow, city_aqi, category)
        text_shadow = ''

    with col5:
        city = 'Mumbai'
        city_aqi = requests.get(f"http://api.waqi.info/feed/{city}/?token={API_KEY}").json()['data']['aqi']
        city_print(city)
        color, category = get_aqi_color(city_aqi)
        if color == '#FFFF00':
            text_shadow = 'text-shadow: -0.75px -0.75px 0 black, 0.75px -0.75px 0 black, -0.75px 0.75px 0 black, 0.75px 0.75px 0 black;'
        aqi_print(color, text_shadow, city_aqi, category)
        text_shadow = ''

    with col6:
        city = 'Beijing'
        city_aqi = requests.get(f"http://api.waqi.info/feed/{city}/?token={API_KEY}").json()['data']['aqi']
        city_print(city)
        color, category = get_aqi_color(city_aqi)
        if color == '#FFFF00':
            text_shadow = 'text-shadow: -0.75px -0.75px 0 black, 0.75px -0.75px 0 black, -0.75px 0.75px 0 black, 0.75px 0.75px 0 black;'
        aqi_print(color, text_shadow, city_aqi, category)
        text_shadow = ''

    # HTML code for AQI category table
    html_table = """
    <table style="border-collapse: collapse; width: 100%; font-family: Arial, sans-serif;">
        <tr style="background-color: #b8b8b8;">
            <th style="border: 1px solid #000; padding: 10px; text-align: center;">AQI</th>
            <th style="border: 1px solid #000; padding: 10px; text-align: center;">Air Pollution Level</th>
            <th style="border: 1px solid #000; padding: 10px; text-align: center;">Health Implications</th>
            <th style="border: 1px solid #000; padding: 10px; text-align: center;">Cautionary Statement (for PM2.5)</th>
        </tr>
        <tr style="background-color: #00e400;">
            <td style="border: 1px solid #000; padding: 10px; text-align: center;">0-50</td>
            <td style="border: 1px solid #000; padding: 10px; text-align: center;">Good</td>
            <td style="border: 1px solid #000; padding: 10px;">Air quality is considered satisfactory, and air pollution poses little or no risk</td>
            <td style="border: 1px solid #000; padding: 10px;">None</td>
        </tr>
        <tr style="background-color: #ffff00;">
            <td style="border: 1px solid #000; padding: 10px; text-align: center;">51-100</td>
            <td style="border: 1px solid #000; padding: 10px; text-align: center;">Moderate</td>
            <td style="border: 1px solid #000; padding: 10px;">Air quality is acceptable; however, for some pollutants, there may be a moderate health concern for a very small number of people who are unusually sensitive to air pollution.</td>
            <td style="border: 1px solid #000; padding: 10px;">Active children and adults, and people with respiratory disease, such as asthma, should limit prolonged outdoor exertion.</td>
        </tr>
        <tr style="background-color: #ff7e00;">
            <td style="border: 1px solid #000; padding: 10px; text-align: center;">101-150</td>
            <td style="border: 1px solid #000; padding: 10px; text-align: center;">Unhealthy for Sensitive Groups</td>
            <td style="border: 1px solid #000; padding: 10px;">Members of sensitive groups may experience health effects. The general public is not likely to be affected.</td>
            <td style="border: 1px solid #000; padding: 10px;">Active children and adults, and people with respiratory disease, such as asthma, should limit prolonged outdoor exertion.</td>
        </tr>
        <tr style="background-color: #ff0000;">
            <td style="border: 1px solid #000; padding: 10px; text-align: center;">151-200</td>
            <td style="border: 1px solid #000; padding: 10px; text-align: center;">Unhealthy</td>
            <td style="border: 1px solid #000; padding: 10px;">Everyone may begin to experience health effects; members of sensitive groups may experience more serious health effects.</td>
            <td style="border: 1px solid #000; padding: 10px;">Active children and adults, and people with respiratory disease, such as asthma, should avoid prolonged outdoor exertion; everyone else, especially children, should limit prolonged outdoor exertion.</td>
        </tr>
        <tr style="background-color: #8f3f97;">
            <td style="border: 1px solid #000; padding: 10px; text-align: center;">201-300</td>
            <td style="border: 1px solid #000; padding: 10px; text-align: center;">Very Unhealthy</td>
            <td style="border: 1px solid #000; padding: 10px;">Health warnings of emergency conditions. The entire population is more likely to be affected.</td>
            <td style="border: 1px solid #000; padding: 10px;">Active children and adults, and people with respiratory disease, such as asthma, should avoid all outdoor exertion; everyone else, especially children, should limit outdoor exertion.</td>
        </tr>
        <tr style="background-color: #7e0023;">
            <td style="border: 1px solid #000; padding: 10px; text-align: center;">300+</td>
            <td style="border: 1px solid #000; padding: 10px; text-align: center;">Hazardous</td>
            <td style="border: 1px solid #000; padding: 10px;">Health alert: everyone may experience more serious health effects.</td>
            <td style="border: 1px solid #000; padding: 10px;">Everyone should avoid all outdoor exertion.</td>
        </tr>
    </table>
    """

    # for space
    st.title('')
    st.title('')
    st.markdown("""
    <div>
    <h2 style="">About the Air Quality and Pollution Measurement:</h2>
    </div>
    """, unsafe_allow_html=True)
    st.markdown(html_table, unsafe_allow_html=True)


api_main()
