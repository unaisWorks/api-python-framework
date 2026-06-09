from utils.logger import get_logger
import pytest

@pytest.mark.api
@pytest.mark.regression
def test_get_user_page_2(client):
    logger = get_logger(__name__)
    logger.info("Starting test_get_user_page_2")
    response = client.get_users_by_page(2)
    body = response.json()

    assert response.status_code == 200
    assert body["page"] == 2

    logger.info("Test Passed")

