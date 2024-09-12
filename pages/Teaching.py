import streamlit as st
import time
import numpy as np
from streamlit_option_menu import option_menu
from streamlit_extras.switch_page_button import switch_page
from streamlit_image_select import image_select
from ppt_utils import *
import os
from stqdm import stqdm

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


with st.form('my_form'):

    img = image_select(
        label="Select a template",
        images=[
            "images/Design-2.png",
            "images/Design-4.png",
            "images/Design-6.png",
            "images/Design-7.png",
        ],
        captions=["Template 1", "Template 2", "Template 3", "Template 4"],
        return_value="index"
    )

    
    if os.getenv("OPEN_AI_KEY") == None:
        openaipass = st.text_input(label='OpenAI Key', type="password", placeholder="Place your OpenAI key here.")
    else:
        openaipass = os.getenv("OPEN_AI_KEY")
    topic = st.text_input(label='Topic of Presentation', value='The Solar System 🌌🚀', placeholder="Topic Name")
    audience = st.text_input(label='Audience for Presentation', value='Middle-school students', placeholder="Who is this meant for?")
    number_slides = st.slider("Number of Slides", 2, 7)
    submitted = st.form_submit_button('Make Presentation!')

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


try:
    pptx = open("generated-ppt/generated_presentation.pptx", "rb")
    st.download_button(label='Download your presentation!', file_name=str(final_slliii[0]["title"] + ".pptx"), data=pptx, mime="application/vnd.ms-powerpoint")
except:
    pass

# Streamlit widgets automatically run the script from top to bottom. Since
# this button is not connected to any other logic, it just causes a plain
# rerun.
