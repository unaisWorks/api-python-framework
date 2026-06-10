from utils.logger import get_logger
from utils.validator import validate_json
import allure
import pytest
from utils.allure_helper import attach_response

@pytest.mark.api
@pytest.mark.regression
@pytest.mark.smoke
@allure.title("Successfully fetched user")
def test_get_user(client):
    logger = get_logger(__name__)
    logger.info("Starting test_get_user")
    response = client.get_single_user(2)

    body = response.json()

    attach_response(response, "Users Response Body")
    assert response.status_code == 200
    assert body["data"]["id"] == 2
    assert body ["data"]["email"] is not None
    assert body ["data"]["first_name"] == "Janet"
    assert response.elapsed.total_seconds() < 3

    logger.info("✓ Test passed")

    validate_json(
        "schemas/user_schema.json",
        response.json()
    )