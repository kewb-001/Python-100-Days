from pathlib import Path
import pytest

from framework.utils.data_loader import DataLoader


@pytest.fixture(scope="session")
def login_data():
    file_path = Path(__file__).resolve().parents[1] / "data" / "login_data.yaml"
    return DataLoader.load_yaml(file_path)
