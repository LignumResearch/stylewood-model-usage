import streamlit as st
import page_about
import page_gui
import page_instructions

st.set_page_config(page_title = "StyleWood: Web Application GUI", layout = "centered")

st.sidebar.title('Navigation')

with st.sidebar:
    button_about = st.button('About Us')

    button_instructions = st.button('Instructions')

    button_gui = st.button('User GUI')

if(button_about):
    page_about.app()
elif(button_instructions):
    page_instructions.app()
elif(button_gui or not(button_about and button_gui and button_instructions)):
    page_gui.app()
