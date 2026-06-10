from payloads.create_user_payload import create_user_payload
from utils.logger import get_logger
import allure
import pytest
from utils.allure_helper import attach_payload,attach_response

@pytest.mark.api
@pytest.mark.regression
@pytest.mark.smoke
@allure.title("Create a new user successfully")
def test_create_user(client):
    logger = get_logger(__name__)
    logger.info("Starting test_create_user")


    payload = create_user_payload()

    attach_payload(
        payload,
        "Create User Payload"
    )
    response = client.create_user(payload)
    body = response.json()

    attach_response(
        response,
        "Create User Response"
    )
    assert response.status_code == 201

    assert body["name"] == payload["name"]
    assert body["job"] == payload["job"]
    logger.info("Test Passed")

