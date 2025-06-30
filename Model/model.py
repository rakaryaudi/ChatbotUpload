import streamlit as st
from openai import OpenAI


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
            file_batch = self.openai_client.vector_stores.file_batches.upload_and_poll(
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
