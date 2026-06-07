from payloads.create_user_payload import create_user_payload
from utils.logger import get_logger



def test_create_user(client):
    logger = get_logger(__name__)
    logger.info("Starting test_create_user")
    payload = create_user_payload()
    response = client.create_user(payload)
    body = response.json()
    print(response.text)
    assert response.status_code == 201

    assert body["name"] == payload["name"]
    assert body["job"] == payload["job"]
    logger.info("Test Passed")
