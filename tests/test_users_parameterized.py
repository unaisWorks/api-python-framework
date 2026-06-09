from utils.logger import get_logger
from utils.validator import validate_json
import allure
import pytest


@allure.title("Validate Multiple Users")
@pytest.mark.parametrize(
    "user_id",
    [1, 2, 3]
)
@pytest.mark.api
@pytest.mark.regression
def test_get_multiple_users(client,user_id):
    logger = get_logger(__name__)
    logger.info(f"Starting test for user_id={user_id}")
    response = client.get_single_user(user_id)

    allure.attach(
        response.text,
        name= "Response Body",
        attachment_type=allure.attachment_type.JSON
    )

    body = response.json()

    assert response.status_code == 200
    assert body["data"]["id"] == user_id
    assert body ["data"]["email"] is not None

    assert response.elapsed.total_seconds() < 3

    logger.info("✓ Test passed")

    validate_json(
        "schemas/user_schema.json",
        body
    )