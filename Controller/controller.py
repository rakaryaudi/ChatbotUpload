from Model.model import FileModel
from View.view import FileView

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
