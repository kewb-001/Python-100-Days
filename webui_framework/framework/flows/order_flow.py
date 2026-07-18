from framework.components.upload_component import UploadComponent


class OrderFlow:
    def __init__(self, page):
        self.page = page
        self.upload_component = UploadComponent(page)

    def upload_attachment(self, file_path: str):
        self.upload_component.upload(file_path)
        return self
