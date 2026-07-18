from pathlib import Path

import pytest

from framework.flows.auth_flow import AuthFlow
from framework.utils.data_loader import DataLoader


DATA_FILE = Path(__file__).resolve().parents[1] / "framework" / "data" / "login_data.yaml"
CASES = DataLoader.load_yaml(DATA_FILE).get("valid_cases", [])


def _build_login_html():
    return """
    <div data-testid='global-modal' style='display:block'>
      <button data-testid='modal-close' onclick="document.querySelector('[data-testid=global-modal]').style.display='none'">X</button>
    </div>
    <input id='username' />
    <input id='password' type='password' />
    <button id='submit' onclick="document.getElementById('welcome').innerText='welcome:'+document.getElementById('username').value">登录</button>
    <div id='welcome'></div>
    """


@pytest.mark.parametrize("case", CASES, ids=[c["case_id"] for c in CASES])
def test_login_success(page, case):
    page.set_content(_build_login_html())
    flow = AuthFlow(page)
    result = flow.login_as(case["username"], case["password"])
    assert result == f"welcome:{case['username']}"
