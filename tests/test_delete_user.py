from utils.logger import get_logger

def test_delete_user(client):
    logger = get_logger(__name__)
    logger.info("Starting test_delete_user")
    response = client.delete_user(3)

    assert response.status_code == 204
    assert response.text == ""
    logger.info("Test Passed")