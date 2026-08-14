from jsonschema import validate
import requests
from schemas import USER_DETAIL_SCHEMA

def test_user_detail_schema(base_url, api_headers):
    url = f"{base_url}/api/users/2"
    response = requests.get(url, headers=api_headers)

    assert response.status_code == 200

    validate(instance=response.json(), schema=USER_DETAIL_SCHEMA)