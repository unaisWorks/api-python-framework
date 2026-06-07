import requests

from config.config import BASE_URL
from api_clients.base_client import BaseClient
from utils.logger import log_response, log_request, get_logger


class UsersClient(BaseClient):
#used path parameters

    def get_single_user(self, user_id):
        log_request(self.logger, "GET", f"{BASE_URL}/users/{user_id}")
        response = self.session.get(
            f"{BASE_URL}/users/{user_id}",
        )
        log_response(self.logger, response.status_code, response.elapsed.total_seconds(), response.json())
        return response
#Using Query parameter
    def get_users_by_page(self, page):

        log_request(self.logger, "GET", f"{BASE_URL}/users")
        response = self.session.get(
            f"{BASE_URL}/users",
            params={"page":page}
        )

        log_response(self.logger, response.status_code, response.elapsed.total_seconds(), response.json())
        return response

    def create_user(self,payload):
        log_request(
            self.logger,
            "POST",
            f"{BASE_URL}/users"
        )

        response = self.session.post(
            f"{BASE_URL}/users",
            json=payload
        )

        log_response(
            self.logger,
            response.status_code,
            response.elapsed.total_seconds(),
            response.json()
        )

        return response

    def update_user(self,user_id, payload):
        log_request(self.logger, "PUT",f"{BASE_URL}/users/{user_id}" )
        response = self.session.put(
            f"{BASE_URL}/users/{user_id}",
            json=payload
        )
        log_response(
            self.logger,
            response.status_code,
            response.elapsed.total_seconds(),
            response.json()
        )
        return response

    def patch_user(self,user_id, payload):
        log_request(self.logger, "PATCH", f"{BASE_URL}/users/{user_id}")
        response = self.session.patch(
            f"{BASE_URL}/users/{user_id}",
            json=payload
        )
        log_response(
            self.logger,
            response.status_code,
            response.elapsed.total_seconds(),
            response.json()
        )
        return response

    def delete_user(self,user_id):
        log_request(self.logger, "DELETE", f"{BASE_URL}/users/{user_id}")
        response = self.session.delete(
            f"{BASE_URL}/users/{user_id}",
        )

        log_response(
            self.logger,
            response.status_code,
            response.elapsed.total_seconds()
        )
        return response