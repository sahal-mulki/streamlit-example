import streamlit as st
import pandas as pd
import pydeck as pdk
from urllib.error import URLError
from streamlit_option_menu import option_menu
from streamlit_extras.switch_page_button import switch_page
from stqdm import stqdm
from worksheet_utils import *
from zipfile import ZipFile
import os

os.system("rm " + "generated-question-sheets/*.docx")
os.system("rm " + "generated-answer-sheets/*.docx")
os.system("rm " + "worksheets.zip")

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
    number_questions = st.slider("Number of Questions", 2, 15)
    submitted = st.form_submit_button('Make Worksheet!')

    if not openaipass.startswith('sk-'):
        st.warning('Please enter your OpenAI API key!', icon='⚠')
    if submitted and openaipass.startswith('sk-'):
        with stqdm(total=100) as pbar:
            pbar.update(5)
            st.toast('Starting creation.', icon='✔️')
            questions = create_worksheet_layout(topic, audience, number_questions, openaipass)
            pbar.update(50)
            st.toast('Questions and answers made, proceeding to title.', icon='📔')

            questions, questions_spaces, answers = process_output_worksheet(questions, number_questions)
            title = make_sheet_title(topic, audience, openaipass)

            pbar.update(30)

            st.toast('Title created.', icon='🎛️')

            st.toast('Starting Word file creation!', icon='✔️')

            path_answer_sheet = make_question_sheet(title, questions, questions_spaces)
            path_question_sheet = make_answer_sheet(title, questions, answers)

            zipObj = ZipFile("worksheets.zip", "w")
            # Add multiple files to the zip
            zipObj.write(path_answer_sheet)
            zipObj.write(path_question_sheet)
            # close the Zip File
            zipObj.close()


            st.toast('Your Question Sheet and Answer Sheet is ready for download!', icon='✔️')

try:
    answer_sheet = open("worksheets.zip", "r")
    #question_sheet = open(path_question_sheet, "rb")
    #st.download_button(label='Download your question sheet!', file_name=str(title + " - QUESTION SHEET" + '.docx'), data=question_sheet, mime="application/vnd.openxmlformats-officedocument.wordprocessingml.document")
    st.download_button(label='Download your documents!', file_name=str(title + "Worksheets - TutorBuddy" + '.zip'), data=answer_sheet, mime="application/zip")
except Exception as fnf_error:
    print(fnf_error)
