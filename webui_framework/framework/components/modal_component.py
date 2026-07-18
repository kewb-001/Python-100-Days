from framework.core.base_page import BasePage


class ModalComponent(BasePage):
    modal = "[data-testid='global-modal']"
    close_btn = "[data-testid='modal-close']"

    def is_visible(self) -> bool:
        return self.page.locator(self.modal).is_visible()

    def close_if_present(self):
        if self.is_visible():
            self.click(self.close_btn)
        return self
