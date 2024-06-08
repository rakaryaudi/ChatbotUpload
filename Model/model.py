import streamlit as st
from openai import OpenAI


class FileModel:
    def __init__(data):
        data.api_key = st.secrets["API_KEY"]
        data.assistant_id = st.secrets["ASSISTANT_ID"]
        data.vector_store_id = st.secrets["VECTOR_ID"]
        data.openai_client = OpenAI(api_key=data.api_key)
        data.accepted_file_types = ["pdf", "doc", "docx", "ppt", "pptx"]
    
    def upload_file(data, uploaded_file):
        file_extension = uploaded_file.name.split(".")[-1].lower()
        if file_extension in data.accepted_file_types:
            file_batch = data.openai_client.beta.vector_stores.file_batches.upload_and_poll(
                vector_store_id=data.vector_store_id,
                files=[uploaded_file]
            )

            data.openai_client.beta.assistants.update(
                assistant_id=data.assistant_id,
                tool_resources={"file_search": {"vector_store_ids": [data.vector_store_id]}}
            )
            return True
        else:
            return False
