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

@pytest.fixture
def auth_token(base_url, api_headers):
    """Fixture return Auth Token"""
    url = f"{base_url}/api/login"
    payload = {
        "email": "eve.holt@reqres.in",
        "password": "cityslicka"
    }

    response = requests.post(url, headers=api_headers, json=payload)
    token = response.json().get("token")

    print(f"\n Get token success: {token}")
    return token
    
