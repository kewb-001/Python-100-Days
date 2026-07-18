from pathlib import Path
import re

import pytest

from framework.fixtures.browser_fixtures import *  # noqa: F401,F403
from framework.fixtures.data_fixtures import *  # noqa: F401,F403
from framework.utils.time_util import timestamp
from framework.utils.paths import SCREENSHOT_DIR, ensure_dirs

import allure


def _safe_name(name: str) -> str:
    return re.sub(r"[^\w.-]+", "_", name)


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()

    if rep.when != "call":
        return

    ensure_dirs()
    page = item.funcargs.get("page")
    if page and rep.failed:
        test_name = _safe_name(item.name)
        screenshot = Path(SCREENSHOT_DIR) / f"{test_name}_{timestamp()}.png"
        page.screenshot(path=str(screenshot), full_page=True)
        allure.attach.file(str(screenshot), name="failure_screenshot", attachment_type=allure.attachment_type.PNG)

    console_file = getattr(item, "_console_file", None)
    if console_file and console_file.exists():
        allure.attach.file(str(console_file), name="console_log", attachment_type=allure.attachment_type.TEXT)

    video_path = getattr(item, "_video_path", None)
    if video_path and Path(video_path).exists():
        allure.attach.file(str(video_path), name="video", attachment_type=allure.attachment_type.WEBM)
