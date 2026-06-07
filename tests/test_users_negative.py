from utils.logger import get_logger

def test_non_existing_user(client):
    logger = get_logger(__name__)
    logger.info("Starting test_non_existing_user")
    response = client.get_single_user(999)

    assert response.status_code == 404

    logger.info("Test passed")
