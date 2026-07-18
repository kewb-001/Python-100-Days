from framework.core.base_page import BasePage


class LoginPage(BasePage):
    username_input = "#username"
    password_input = "#password"
    submit_button = "#submit"

    def login(self, username: str, password: str):
        (
            self.wait_visible(self.username_input)
            .fill(self.username_input, username)
            .fill(self.password_input, password)
            .click(self.submit_button)
        )
        return self
