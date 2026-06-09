from api_clients.base_client import BaseClient
from config.config import BASE_URL

class AuthClient(BaseClient):

    def login(self, email, password):

        response = self.session.post(
            f"{BASE_URL}/login",
            json={
                "email": email,
                "password": password
            }
        )

        return response

