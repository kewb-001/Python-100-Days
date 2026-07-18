# WebUI 自动化框架（Pytest + Playwright）

## 快速开始

```bash
cd webui_framework
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
playwright install chromium
pytest
```

## Allure 报告

```bash
pytest --alluredir=reports/allure-results
allure generate reports/allure-results -o reports/allure-report --clean
allure open reports/allure-report
```

## 脚手架

```bash
python framework/scripts/scaffold.py page Login
python framework/scripts/scaffold.py component Upload
python framework/scripts/scaffold.py flow Auth
python framework/scripts/scaffold.py test login
```
