import streamlit as st
import pandas as pd
import pydeck as pdk
from urllib.error import URLError
from streamlit_option_menu import option_menu
from streamlit_extras.switch_page_button import switch_page
from stqdm import stqdm

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

with st.form('my_form'):


    openaipass = st.text_input(label='OpenAI Key', type="password", placeholder="Place your OpenAI key here.")
    topic = st.text_input(label='Topic of Worksheet', value='The Solar System 🌌🚀', placeholder="Topic Name")
    audience = st.text_input(label='Audience for Worksheet', value='Middle-school students', placeholder="Who is this meant for?")
    number_slides = st.slider("Number of Questions", 2, 15)
    submitted = st.form_submit_button('Make Worksheet!')

    if not openaipass.startswith('sk-'):
        st.warning('Please enter your OpenAI API key!', icon='⚠')
    if submitted and openaipass.startswith('sk-'):
        with stqdm(total=100) as pbar:
            pbar.update(5)
            st.toast('Starting creation.', icon='✔️')
            slides2 = create_layout(number_slides, topic, audience, openaipass)
            pbar.update(30)
            st.toast('Layout made, proceeding to content.', icon='📔')

            slides_detailed = []
            for slide in slides2:
                pbar.update(3)
                slides_detailed_ind = create_content(slides_list_titles=slide, audience=audience, openaikey=openaipass)
                exec("slides_detailed.append(" + slides_detailed_ind + ")", globals())

            st.toast('Content created, finding a font now.', icon='🎛️')
            fonts = create_font_list(topic=topic, audience=audience, openaikey=openaipass)["fonts"]
            pbar.update(20)
            st.toast('Found an appropriate font, starting PowerPoint file creation!', icon='✔️')
            final_slliii = format_slides(slides=slides2, slides_detailed=slides_detailed)
            create_ppt(final_slliii, int(img), final_slliii[0]["title"], fonts)
            st.toast('Your PowerPoint Presentation is ready for download!', icon='✔️')

