from framework.core.base_page import BasePage


class HeaderComponent(BasePage):
    user_name = "[data-testid='header-username']"

    def get_username(self) -> str:
        return self.text(self.user_name)
