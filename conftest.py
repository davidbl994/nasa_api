import pytest
from config.settings import API_KEY

@pytest.fixture(scope="session", autouse=True)
def check_api_key():
    assert API_KEY is not None, "NASA API key is not set!"