import streamlit as st
st.set_page_config(page_title='AQI data', layout="wide")
# Background color theme
page_bg_img = """
<style>
[data-testid="stAppViewContainer"]{
background: linear-gradient(0deg, rgba(34,193,195,0.7090941011235955) 0%, rgba(79,250,76,0.6416783707865168) 100%);
}
</style>
"""

aqi_main = st.Page(
    "views/aqi_main.py",
    title="Home Page",
    default=True,
)
city_data = st.Page(
    "views/city_data.py",
    title="City Data",
)
forecast = st.Page(
    "views/forecast.py",
    title="Pollutant forecast",
)


pg = st.navigation(
    {
        "Application": [aqi_main],
        "City/Forecast": [city_data, forecast],
    }
)


st.logo("assets/profile-pic(2).png")
st.sidebar.markdown("Contact details : ")
st.sidebar.markdown("Sanchit Aggarwal")
st.sidebar.markdown("+91 910169712")
st.sidebar.markdown("sanchit2509@gmail.com")
st.sidebar.markdown("[👨‍💻 Portfolio](https://sanchit-agg.github.io/SanchitAggarwal.github.io/)")

pg.run()

