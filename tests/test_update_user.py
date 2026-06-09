from payloads.update_user_payload import update_user_payload
from utils.logger import get_logger
import allure
import pytest

@pytest.mark.api
@pytest.mark.regression
@allure.title("Successfully updated user")
def test_update_user(client):
    logger = get_logger(__name__)
    logger.info("Starting test_update_user")
    response = client.update_user(2,update_user_payload())

    allure.attach(
        response.text,
        name="Response Body",
        attachment_type=allure.attachment_type.JSON
    )

    assert response.status_code == 200
    body = response.json()

    assert body["name"] == "sam Updated"
    assert body["job"] == "QA Lead"
    assert "updatedAt" in body
    assert response.elapsed.total_seconds() < 2

    logger.info("Test passed")