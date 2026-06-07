# API Automation Framework

## Overview

This project is a REST API Automation Framework built using Python, Requests, and Pytest.

The framework follows a scalable design using the API Client Pattern and is intended for learning and practicing API automation testing concepts.

## Tech Stack

* Python
* Requests
* Pytest
* Faker
* Allure Reporting
* Logging

## Project Structure

```text
api-python-framework
│
├── api_clients/
├── config/
├── payloads/
├── tests/
├── test_data/
├── utils/
│
├── conftest.py
├── pytest.ini
├── requirements.txt
└── README.md
```

## Features Implemented

* GET API Testing
* POST API Testing
* PUT API Testing
* DELETE API Testing
* Positive Test Scenarios
* Negative Test Scenarios
* API Client Pattern
* Request and Response Logging
* Faker Test Data Generation
* Pytest Fixtures

## Run Tests

Install dependencies:

```bash
pip install -r requirements.txt
```

Run tests:

```bash
pytest -v -s
```

## Future Enhancements

* JSON Schema Validation
* Environment Variable Management
* Secrets Handling
* Allure Attachments
* API Chaining
* GitHub Actions CI/CD
* Database Validation
