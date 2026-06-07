import logging
import os
from datetime import datetime

# Create logs directory
LOG_DIR = "reports/logs"
os.makedirs(LOG_DIR, exist_ok=True)

# Create timestamped file
timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")

LOG_FILE = os.path.join(
    LOG_DIR,
    f"test_run_{timestamp}.log"
)

def get_logger(name):

    logger = logging.getLogger(name)

    if logger.handlers:
        logger.handlers.clear()

    logger.setLevel(logging.DEBUG)

    # File Handler
    file_handler = logging.FileHandler(LOG_FILE)
    file_handler.setLevel(logging.DEBUG)

    # Console Handler
    console_handler = logging.StreamHandler()
    console_handler.setLevel(logging.INFO)

    # Formatters
    file_formatter = logging.Formatter(
        "%(asctime)s - %(name)s - %(levelname)s - [%(filename)s:%(lineno)d] - %(message)s"
    )

    console_formatter = logging.Formatter(
        "%(levelname)s - %(name)s - %(message)s"
    )

    file_handler.setFormatter(file_formatter)
    console_handler.setFormatter(console_formatter)

    logger.addHandler(file_handler)
    logger.addHandler(console_handler)

    return logger

def log_request(logger, method, url, headers=None, payload=None):
    """Log API request"""
    logger.info(f"🔵 REQUEST: {method} {url}")
    if payload:
        logger.debug(f"   Payload: {payload}")


def log_response(logger, status_code, response_time, response_body=None):
    """Log API response"""
    status_icon = "✅" if 200 <= status_code < 300 else "❌"
    logger.info(f"{status_icon} RESPONSE: {status_code} | Time: {response_time:.2f}s")
    if response_body:
        logger.debug(f"   Body: {response_body}")