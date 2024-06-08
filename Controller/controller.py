from Model.model import FileModel
from View.view import FileView

class FileController:
    def __init__(data):
        data.model = FileModel()
        data.view = FileView()

    def run(data):
        data.view.render_header()
        uploaded_file = data.view.render_file_uploader()

        if uploaded_file is not None:
            if data.model.upload_file(uploaded_file):
                data.view.show_success("File Sudah Berhasil Ditambahkan")
            else:
                data.view.show_error("Jenis file tidak didukung. Silakan unggah file dalam format PDF, Word, atau PowerPoint.")
        else:
            data.view.show_warning("Silakan unggah file terlebih dahulu.")
