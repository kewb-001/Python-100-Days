from pathlib import Path
import re
import pytest

from playwright.sync_api import sync_playwright

from framework.utils.paths import ensure_dirs, VIDEO_DIR, CONSOLE_DIR


def _safe_name(nodeid: str) -> str:
    return re.sub(r"[^\w.-]+", "_", nodeid)


@pytest.fixture(scope="session")
def playwright_instance():
    with sync_playwright() as p:
        yield p


@pytest.fixture
def page(playwright_instance, request):
    ensure_dirs()
    browser = playwright_instance.chromium.launch(headless=True)
    context = browser.new_context(record_video_dir=str(VIDEO_DIR))
    pg = context.new_page()

    test_name = _safe_name(request.node.name)
    log_file = Path(CONSOLE_DIR) / f"{test_name}.log"
    logs: list[str] = []

    def _on_console(msg):
        logs.append(f"[{msg.type}] {msg.text}")

    pg.on("console", _on_console)
    request.node._console_logs = logs
    request.node._console_file = log_file

    yield pg

    log_file.write_text("\n".join(logs), encoding="utf-8")
    request.node._video_path = pg.video.path() if pg.video else None
    context.close()
    browser.close()
