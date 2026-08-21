import pytest
import requests
from data.test_users_data import CREATE_USER_PAYLOADS

@pytest.mark.parametrize("user_data", CREATE_USER_PAYLOADS)
def test_create_user_data_driven(dummy_base_url, user_data):
    url = f"{dummy_base_url}/users/add"
    response = requests.post(url, json=user_data)

    assert response.status_code in [200, 201]
    data = response.json()
    assert data["firstName"] == user_data["firstName"]
    assert data["lastName"] == user_data["lastName"]
    assert data["age"] == user_data["age"]
    assert "id" in data

def test_filter_users_by_gender(dummy_base_url):
    url = f"{dummy_base_url}/users/filter"
    query_params = {
        "key":"gender",
        "value":"female"
    }
    response = requests.get(url, params=query_params)

    assert response.status_code == 200
    data = response.json()
    users = data.get("users", [])
    assert len(users) > 0
    for user in users:
        assert user.get("gender") == "female"

def test_update_user_info(dummy_base_url):
    url = f"{dummy_base_url}/users/1"
    payload = {
            "lastName": "UpdatedLastName",
            "age": 35
        }
    response = requests.put(url, json=payload)

    assert response.status_code == 200
    data = response.json()
    assert data["lastName"] == "UpdatedLastName"
    assert data["age"] == 35

def test_delete_user(dummy_base_url):
    url = f"{dummy_base_url}/users/1"
    response = requests.delete(url)

    assert response.status_code == 200
    data = response.json()
    assert data.get("isDeleted") is True, f"return value {data.get("isDeleted")}"
    deleted_on = data.get("deletedOn")
    assert deleted_on is not None, "Trường deletedOn không được là None"
    assert deleted_on != "", "Trường deletedOn không được là chuỗi rỗng"

