from config.config import API_KEY
import requests
from utils.logger import get_logger


class BaseClient:

    def __init__(self):
        self.logger = get_logger(__name__)
        self.session = requests.Session()

        if API_KEY:
            self.session.headers.update({
                "x-api-key": API_KEY
            })

        self.logger.info("BaseClient initialized")