import pytest
import requests

def test_get_product_with_pagination(base_url, api_headers, auth_token):
    # used baseURL and APIheaders
    url = f"{base_url}/api/users?page=2"

    headers = api_headers.copy()
    headers["Authorization"] = f"Bearer {auth_token}"
    #Send request GET
    response = requests.get(url, headers=headers)

    #Verify Status code and token
    data = response.json()["data"]
    assert response.status_code == 200
    assert response.json()["page"] == 2
    assert len(data) > 0

    expected_keys = ["id", "email", "first_name", "last_name"]

    for item in data:
        for key in expected_keys:
            assert key in item, f"Thiếu trường '{key}' trong item: {item}"

    print("\n Get Product with Pagniation.")

def test_get_single_product_detail(base_url, api_headers, auth_token):
    url = f"{base_url}/api/users/2"

    headers = api_headers.copy()
    headers["Authorization"] = f"Bearer {auth_token}"

    response = requests.get(url, headers = headers)

    assert response.status_code == 200
    assert response.json()["data"]["id"] == 2

    print("\n Get Single Product Detail success")

