import pytest
import requests

@pytest.mark.parametrize(
    "name, job, expected_status",
    [
        ("John Doe", "Software Engineer", 201),
        ("Alice & Bob", "QA Lead @ TechCorp", 201),
        ("a" * 50, "DevOps", 201)
    ]
)

def test_create_user_data_driven(base_url, api_headers, name, job, expected_status):
    url = f"{base_url}/api/users"
    payload = {"name": name, "job": job}

    response = requests.post(url, headers=api_headers, json=payload)
    assert response.status_code == 201
    assert response.json()["name"] == name
    assert response.json()["job"] == job
    assert "id" in response.json()
    
