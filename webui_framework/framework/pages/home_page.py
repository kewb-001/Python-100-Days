from framework.core.base_page import BasePage


class HomePage(BasePage):
    welcome_text = "#welcome"

    def welcome(self) -> str:
        return self.text(self.welcome_text)
