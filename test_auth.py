import requests
import pytest

def test_login_success(base_url, api_headers):
    # used baseURL and APIheaders
    url = f"{base_url}/api/login"
    payload = {
        "email": "eve.holt@reqres.in",
        "password": "cityslicka"
    }

    #Send request POST
    response = requests.post(url, headers=api_headers, json=payload)

    #Verify Status code and token
    assert response.status_code == 200
    assert "token" in response.json()
    print(f"\n Login success with token: ", response.json()["token"])

def test_missing_passwords(base_url, api_headers):
    # used baseURL and APIheaders
    url = f"{base_url}/api/login"
    payload = {"email": "eve.holt@reqres.in"}

    # Send request POST
    response = requests.post(url, headers=api_headers, json=payload)

    #Verify Status code and token
    assert response.status_code == 400
    assert response.json()["error"] == "Missing password"
    print("\n Catch Missing Passwords")