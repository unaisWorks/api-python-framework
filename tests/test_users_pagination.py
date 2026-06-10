from utils.logger import get_logger
import pytest
from utils.allure_helper import attach_response
import allure

@pytest.mark.api
@pytest.mark.regression
@allure.title("Successfully fetch users on page 2")
def test_get_user_page_2(client):
    logger = get_logger(__name__)
    logger.info("Starting test_get_user_page_2")
    response = client.get_users_by_page(2)
    body = response.json()

    attach_response(response, "Pagination Response")
    assert response.status_code == 200
    assert body["page"] == 2

    logger.info("Test Passed")

