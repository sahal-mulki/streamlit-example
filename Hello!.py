import altair as alt
import numpy as np
import pandas as pd
import streamlit as st
from streamlit_option_menu import option_menu
from streamlit_extras.switch_page_button import switch_page

st.set_page_config(
    page_title="Hello",
    page_icon="👋",
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
            options=["Home", "Teach", "Test"],
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
        if selected == "Teach":
            switch_page("Teaching")
        if selected == "Test":
            switch_page("Testing")


"""
# Welcome to TutorBuddy!

### TutorBuddy is an integrated application to help teachers create learning aids, and test students on information.

### To get started, click the "Teach" Icon to make a learning aid, or "Test" to make an examination sheet!
"""