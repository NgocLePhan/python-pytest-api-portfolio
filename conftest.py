import os
import pytest
import requests
from dotenv import load_dotenv

load_dotenv()

@pytest.fixture
def base_url():
    """Fixture return Base URL"""
    return os.getenv("BASE_URL", "https://reqres.in")

@pytest.fixture
def api_headers():
    """Fixture return API Headers"""
    private_key = os.getenv("API_PRIVATE_KEY", "")
    return{
        "x-api-key": private_key,
        "Conten-Type": "application/json"
    }