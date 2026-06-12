from utils.logger import get_logger
import pytest
from utils.allure_helper import attach_response
import allure

@pytest.mark.api
@pytest.mark.regression
@allure.title("Return 404 for non-existing user")
@allure.feature("User Management")
@allure.severity(allure.severity_level.MINOR)
def test_non_existing_user(client):
    logger = get_logger(__name__)
    logger.info("Starting test_non_existing_user")
    response = client.get_single_user(999)

    attach_response(response,"Non-Existing User Response")
    assert response.status_code == 404

    logger.info("Test passed")
