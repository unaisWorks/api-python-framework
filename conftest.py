import pytest
from api_clients.users_client import UsersClient

# Configure pytest logging
def pytest_configure(config):
    config.option.log_cli = True  # Show logs in console
    config.option.log_cli_level = "INFO"  # Set log level

@pytest.fixture(scope="session")
def client():
    return UsersClient()
