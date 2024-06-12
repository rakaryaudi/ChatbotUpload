from io import BytesIO
import requests
import streamlit as st
from PIL import Image

class FileView:
    def __init__(data):
        st.set_page_config(page_title="Upload File Pembelajaran Sistem Basis Data", page_icon=":books:")

    def render_header(data):
        logo_url = "https://github.com/GabrielDFA/Tia-Chatbot/blob/e0f2ec150495c0298da9b9e9ec1f50a71e41333b/Asset/logo.png?raw=true"
        response = requests.get(logo_url)
        logo = Image.open(BytesIO(response.content))
        col1, col2 = st.columns([1, 7])
        with col1:
            st.image(logo, width=80)
        with col2:
            st.title("Upload Materi Sistem Basis Data👋")

    def render_file_uploader(data):
        return st.file_uploader("Upload File Pembelajaran Sistem Basis Data🖥️", type=["pdf", "doc", "docx", "ppt", "pptx"])

    def show_success(data, message):
        st.success(message)

    def show_error(data, message):
        st.error(message)

    def show_warning(data, message):
        st.warning(message)
