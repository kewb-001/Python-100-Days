from pathlib import Path
from playwright.sync_api import Page, FrameLocator


class BasePage:
    def __init__(self, page: Page):
        self.page = page

    def click(self, locator: str, timeout: int = 10000):
        self.page.locator(locator).click(timeout=timeout)
        return self

    def fill(self, locator: str, value: str, timeout: int = 10000):
        self.page.locator(locator).fill(value, timeout=timeout)
        return self

    def text(self, locator: str, timeout: int = 10000) -> str:
        self.page.locator(locator).wait_for(state="visible", timeout=timeout)
        return self.page.locator(locator).inner_text()

    def wait_visible(self, locator: str, timeout: int = 10000):
        self.page.locator(locator).wait_for(state="visible", timeout=timeout)
        return self

    def wait_clickable(self, locator: str, timeout: int = 10000):
        self.page.locator(locator).wait_for(state="visible", timeout=timeout)
        self.page.locator(locator).is_enabled(timeout=timeout)
        return self

    def wait_for_network_idle(self, timeout: int = 10000):
        self.page.wait_for_load_state("networkidle", timeout=timeout)
        return self

    def get_frame(self, selector: str) -> FrameLocator:
        return self.page.frame_locator(selector)

    def screenshot(self, path: str | Path):
        self.page.screenshot(path=str(path), full_page=True)
        return self
