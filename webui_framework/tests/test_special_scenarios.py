from framework.components.upload_component import UploadComponent
from framework.core.base_page import BasePage


def test_iframe_interaction(page):
    page.set_content(
        """
        <iframe id='login-frame' srcdoc="<button id='inner-btn' onclick=\"document.body.setAttribute('data-clicked','yes')\">ok</button>"></iframe>
        """
    )
    bp = BasePage(page)
    frame = bp.get_frame("#login-frame")
    frame.locator("#inner-btn").click()
    assert frame.locator("body").get_attribute("data-clicked") == "yes"


def test_upload_file(page, tmp_path):
    file_path = tmp_path / "demo.txt"
    file_path.write_text("demo", encoding="utf-8")
    page.set_content("<input type='file' />")
    upload = UploadComponent(page)
    upload.upload(str(file_path))
    assert page.locator("input[type='file']").evaluate("e => e.files.length") == 1


def test_slow_loading_wait(page):
    page.set_content("<button id='later' style='display:none'>later</button>")
    page.evaluate("setTimeout(() => document.getElementById('later').style.display='block', 300)")
    bp = BasePage(page)
    bp.wait_visible("#later", timeout=2000)
    assert page.locator("#later").is_visible()
