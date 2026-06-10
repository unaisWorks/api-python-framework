from payloads.update_user_payload import update_user_payload
from utils.logger import get_logger
import allure
import pytest
from utils.allure_helper import attach_response,attach_payload

@pytest.mark.api
@pytest.mark.regression
@allure.title("Successfully updated user")
def test_update_user(client):
    logger = get_logger(__name__)
    logger.info("Starting test_update_user")
    payload = update_user_payload()
    attach_payload(payload,"Update User Payload")
    response = client.update_user(2,payload)

    assert response.status_code == 200
    body = response.json()

    attach_response(response, "Update user Response")

    assert body["name"] == "sam Updated"
    assert body["job"] == "QA Lead"
    assert "updatedAt" in body
    assert response.elapsed.total_seconds() < 2

    logger.info("Test passed")