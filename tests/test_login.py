from api_clients.auth_client import AuthClient
import pytest

@pytest.mark.api
@pytest.mark.regression
@pytest.mark.smoke
def test_login(client):

    auth_client = AuthClient()

    login_response = auth_client.login(
        "eve.holt@reqres.in",
        "cityslicka"
    )

    assert login_response.status_code == 200

    token = login_response.json()["token"]

    print(token)