import streamlit as st
import pandas as pd
import pydeck as pdk
from urllib.error import URLError
from streamlit_option_menu import option_menu
from streamlit_extras.switch_page_button import switch_page

st.set_page_config(page_title="Testing", page_icon="🎓📝",
    initial_sidebar_state="collapsed")

st.markdown(
    """
<style>
    [data-testid="collapsedControl"] {
        display: none
    }
</style>
""",
    unsafe_allow_html=True,
)

with st.container():
        selected = option_menu(
            menu_title=None,
            options=["Test", "Teach", "Home"],
            icons=['house', 'highlighter', "bi-clipboard2-check"],
            menu_icon="cast",
            orientation="horizontal",
            styles={
                "nav-link": {
                    "text-align": "center",
                    "--hover-color": "#eee",
                }
            }
        )
        if selected == "Home":
            switch_page("Hello!")
        if selected == "Teach":
            switch_page("Teaching")



st.markdown("# Testing")
st.sidebar.header("Testing")
st.write(
    """This demo is going to make an examination question paper and answer. Just provide the topic, audience, and number of slides, and you're good to go!"""
)


topic = st.text_input(label='Topic of Worksheet', value='The Solar System 🌌🚀', placeholder="Topic Name")
audience = st.text_input(label='Audience for Worksheet', value='Middle-school students', placeholder="Who is this meant for?")
number_slides = st.slider("Number of Questions", 2, 15)
