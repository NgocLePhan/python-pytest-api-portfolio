import pytest
import requests

# Step 1
def test_API_chaining(base_url,api_headers,auth_token):
    urlPost = f"{base_url}/api/users"
    payloadPost = {
        "name": "morpheus",
        "job": "leader"   
    }

    responsePost = requests.post(urlPost, headers=api_headers, json=payloadPost)

    assert responsePost.status_code == 201
    assert responsePost.json()["name"] == "morpheus"
    assert responsePost.json()["job"] == "leader"

    bodyPost = responsePost.json()
    assert "id" in bodyPost, "Response Post không có trường 'id'"
    assert "createdAt" in bodyPost, "Response Post không có trường 'createdAt'"
    
    user_id = responsePost.json()["id"]

    urlPut = f"{base_url}/api/users/{user_id}"
    payloadPut = {
        "name": "morpheus",
        "job": "zion resident"
    }

    responsePut = requests.put(urlPut, headers=api_headers, json=payloadPut)

    assert responsePut.status_code == 200
    assert responsePut.json()["job"] == "zion resident"

    bodyPut = responsePut.json()
    assert "updatedAt" in bodyPut, "Response Put không có trường 'createdAt'"

    urlDelete = f"{base_url}/api/users/{user_id}"

    respnseDelete = requests.delete(urlDelete, headers=api_headers)

    assert respnseDelete.status_code == 204