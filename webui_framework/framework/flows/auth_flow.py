from framework.pages.login_page import LoginPage
from framework.pages.home_page import HomePage
from framework.components.modal_component import ModalComponent


class AuthFlow:
    def __init__(self, page):
        self.page = page
        self.login_page = LoginPage(page)
        self.home_page = HomePage(page)
        self.modal = ModalComponent(page)

    def login_as(self, username: str, password: str) -> str:
        self.modal.close_if_present()
        self.login_page.login(username, password)
        return self.home_page.welcome()
