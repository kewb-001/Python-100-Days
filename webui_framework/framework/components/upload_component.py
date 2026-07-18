from pathlib import Path
from framework.core.base_page import BasePage


class UploadComponent(BasePage):
    file_input = "input[type='file']"

    def upload(self, file_path: str, trigger_selector: str | None = None):
        resolved = str(Path(file_path).resolve())
        if trigger_selector:
            with self.page.expect_file_chooser() as fc_info:
                self.click(trigger_selector)
            fc_info.value.set_files(resolved)
        else:
            self.page.set_input_files(self.file_input, resolved)
        return self
