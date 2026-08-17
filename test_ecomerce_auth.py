import pytest
import requests

def test_ecommerce_login_success(dummy_base_url):
    url = f"{dummy_base_url}/auth/login"
    payload = {
        "username": "emilys",
        "password": "emilyspass",
        "expiresInMins": 30
    }

    response = requests.post(url, json=payload)

    assert response.status_code == 200
    assert "accessToken" in response.json()
    token = response.json()["accessToken"]
    print(f"\nLogin successful with token:{token}")

def test_ecommerce_get_current_user_profile(dummy_base_url, dummy_auth_token):
    url = f"{dummy_base_url}/auth/me"
    headers = {
        "Authorization": f"Bearer {dummy_auth_token}"
    }

    response = requests.get(url, headers=headers)

    assert response.status_code == 200
    assert response.json()["username"] == "emilys"
    print(f"\nGet User success with:", response.json()["username"])

def test_ecommerce_login_invalid_credentials(dummy_base_url):
    url = f"{dummy_base_url}/auth/login"
    payload = {
        "username": "emilys",
        "password": " ",
        "expiresInMins": 30
    }

    response = requests.post(url, json=payload)

    assert response.status_code == 400
    assert response.json()["message"] == "Invalid credentials"