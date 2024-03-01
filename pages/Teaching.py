import streamlit as st
import time
import numpy as np
from streamlit_option_menu import option_menu
from streamlit_extras.switch_page_button import switch_page
from streamlit_image_select import image_select

st.set_page_config(page_title="Teaching", page_icon="👨‍🏫👩‍🏫", initial_sidebar_state="collapsed")

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
            options=["Teach", "Test", "Home"],
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
        if selected == "Test":
            switch_page("Testing")

st.markdown("# Teaching Mode")
st.sidebar.header("Plotting Demo")
st.write(
    """This demo is going to make a PowerPoint Presentation based on any topic you want!
    Just input the topic you want, number of slides, and the audience you want your presentation for (e.g. middle school students), and you're ready to go!"""
)


img = image_select(
    label="Select a template",
    images=[
        "images/Design-2.png",
        "images/Design-4.png",
        "images/Design-6.png",
        "images/Design-7.png",
    ],
    captions=["Template 1", "Template 2", "Template 3", "Template 4"],
)

topic = st.text_input(label='Topic of Presentation', value='The Solar System 🌌🚀', placeholder="Topic Name")
audience = st.text_input(label='Audience for Presentation', value='Middle-school students', placeholder="Who is this meant for?")
number_slides = st.slider("Number of Slides", 2, 15)

# Streamlit widgets automatically run the script from top to bottom. Since
# this button is not connected to any other logic, it just causes a plain
# rerun.
st.button("Re-run")
