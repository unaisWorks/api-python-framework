# API Automation Framework

## Overview

This is a REST API test automation framework built with Python, Requests, and Pytest.
It tests the [Reqres](https://reqres.in) public API and covers real-world patterns
used in professional QA automation — client abstraction, test data generation,
schema validation, structured logging, and Allure reporting.

Built as part of my automation learning journey and portfolio.

## Tech Stack

| Tool | Purpose |
|---|---|
| Python | Core language |
| Requests | HTTP client |
| Pytest | Test runner |
| Allure | Test reporting |
| Faker | Dynamic test data generation |
| jsonschema | Response schema validation |
| python-dotenv | Environment config management |
| Logging | Request/response logging |

## Project Structure

```text
api-python-framework/
│
├── api_clients/
│   ├── base_client.py        # Shared session, auth headers
│   └── users_client.py       # All /users API methods
│
├── config/
│   └── config.py             # Loads env variables
│
├── payloads/
│   ├── create_user_payload.py
│   ├── update_user_payload.py
│   └── patch_user_payload.py
│
├── schemas/
│   └── user_schema.json      # JSON Schema for response validation
│
├── tests/
│   ├── test_users.py          # GET single user
│   ├── test_create_user.py    # POST create user
│   ├── test_update_user.py    # PUT update user
│   ├── test_delete_user.py    # DELETE user
│   ├── test_users_negative.py # Negative scenarios
│   └── test_users_pagination.py # Pagination
│
├── utils/
│   ├── allure_helper.py      # Reusable Allure attachment helpers
│   ├── data_generator.py     # Faker-based user data generator
│   ├── logger.py             # Console + file logging
│   └── validator.py          # JSON schema validation wrapper
│
├── reports/
│   └── logs/                 # Timestamped log files per test run
│
├── conftest.py               # Session-scoped client fixture
├── .env.example              # Environment variable template
├── requirements.txt
└── README.md

Features

Full CRUD coverage — GET, POST, PUT, PATCH, DELETE
Positive and negative test scenarios
Pagination testing
API Client Pattern — BaseClient handles session and auth, UsersClient extends it
Dynamic test data using Faker
JSON Schema validation on responses
Allure reporting with titles, features, severity levels and request/response attachments
Dual logging — console output and timestamped log file per run
Environment config via .env file
Pytest markers — smoke, regression, api

Setup

1. Clone the repo
git clone https://github.com/yourusername/api-python-framework.git
cd api-python-framework

2. Create a virtual environment
python -m venv venv
source venv/bin/activate        # Mac/Linux
venv\Scripts\activate           # Windows

3. Install dependencies
pip install -r requirements.txt

4. Configure environment
cp .env.example .env
Add your API key to the .env file.

Running Tests

Run all tests:
pytest -v

Run by marker:
pytest -m smoke
pytest -m regression
pytest -m api

Run with Allure report:
pytest --alluredir=reports/allure-results
allure serve reports/allure-results
Allure Report

The Allure report shows:
Test results grouped by feature and severity
Request payload attached per test
Response body attached per test
Step-level visibility into each test
To use Allure, install the CLI: brew install allure (Mac)

Environment Variables
Variable	Description
BASE_URL	API base URL
API_KEY	API key for authentication
See .env.example for reference.

What Included in this Framework
How to structure a Python API test framework from scratch
The API Client Pattern and why it matters for scalability
How to separate concerns — clients, payloads, utils, tests
Allure reporting and making reports useful, not just pretty
Real-world practices like schema validation and environment config

Author
Mohamed unais
https://www.linkedin.com/in/unaisvds/
https://github.com/unaisWorks