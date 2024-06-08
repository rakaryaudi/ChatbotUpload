import streamlit as st
from PIL import Image

class FileView:
    def __init__(data):
        st.set_page_config(page_title="Upload File Pembelajaran TIA", page_icon=":books:")

    def render_header(data):
        logo = Image.open(r"Assets\logo.png")
        col1, col2 = st.columns([1, 7])
        with col1:
            st.image(logo, width=80)
        with col2:
            st.title("Chatbot TIA 👋")

    def render_file_uploader(data):
        return st.file_uploader("Upload File Pembelajaran Sistem Basis Data🖥️", type=["pdf", "doc", "docx", "ppt", "pptx"])

    def show_success(data, message):
        st.success(message)

    def show_error(data, message):
        st.error(message)

    def show_warning(data, message):
        st.warning(message)
