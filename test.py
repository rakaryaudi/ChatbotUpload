import streamlit as st
from openai import OpenAI
from io import BytesIO
import requests
from PIL import Image

class FileModel:
    def __init__(self):
        self.api_key = st.secrets["API_KEY"]
        self.assistant_id = st.secrets["ASSISTANT_ID"]
        self.vector_store_id = st.secrets["VECTOR_ID"]
        self.openai_client = OpenAI(api_key=self.api_key)
        self.accepted_file_types = ["pdf", "doc", "docx", "ppt", "pptx"]
    
    def upload_file(self, uploaded_file):
        file_extension = uploaded_file.name.split(".")[-1].lower()
        if file_extension in self.accepted_file_types:
            file_batch = self.openai_client.beta.vector_stores.file_batches.upload_and_poll(
                vector_store_id=self.vector_store_id,
                files=[uploaded_file]
            )

            self.openai_client.beta.assistants.update(
                assistant_id=self.assistant_id,
                tool_resources={"file_search": {"vector_store_ids": [self.vector_store_id]}}
            )
            return True
        else:
            return False

class FileView:
    def __init__(self):
        st.set_page_config(page_title="Upload File Pembelajaran Sistem Basis Data", page_icon=":books:")

    def render_header(self):
        logo_url = "https://github.com/GabrielDFA/Tia-Chatbot/blob/e0f2ec150495c0298da9b9e9ec1f50a71e41333b/Asset/logo.png?raw=true"
        response = requests.get(logo_url)
        logo = Image.open(BytesIO(response.content))
        col1, col2 = st.columns([1, 7])
        with col1:
            st.image(logo, width=80)
        with col2:
            st.title("Upload Materi Sistem Basis Data👋")

    def render_file_uploader(self):
        return st.file_uploader("Upload File Pembelajaran Sistem Basis Data🖥️", type=["pdf", "doc", "docx", "ppt", "pptx"])

    def show_success(self, message):
        st.success(message)

    def show_error(self, message):
        st.error(message)

    def show_warning(self, message):
        st.warning(message)

class FileController:
    def __init__(self):
        self.model = FileModel()
        self.view = FileView()

    def run(self):
        self.view.render_header()
        uploaded_file = self.view.render_file_uploader()

        if uploaded_file is not None:
            if self.model.upload_file(uploaded_file):
                self.view.show_success("File Sudah Berhasil Ditambahkan")
            else:
                self.view.show_error("Jenis file tidak didukung. Silakan unggah file dalam format PDF, Word, atau PowerPoint.")
        else:
            self.view.show_warning("Silakan unggah file terlebih dahulu.")

if __name__ == "__main__":
    controller = FileController()
    controller.run()
