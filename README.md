# API Automation Framework

## Overview

This is a REST API test automation framework built using Python, Requests, and Pytest.

The framework uses the ReqRes public API for demonstration purposes and showcases real-world API automation practices used in professional QA and SDET teams, including client abstraction, dynamic test data generation, schema validation, structured logging, environment management, and rich reporting.

Although ReqRes is used as the target API, the framework architecture is designed to be reusable and scalable for real-world REST API testing projects.

This project was built as part of my QA Automation learning journey and portfolio development.

---

## Tech Stack

| Tool           | Purpose                              |
| -------------- | ------------------------------------ |
| Python         | Core programming language            |
| Requests       | HTTP client for API interactions     |
| Pytest         | Test runner and framework            |
| Allure         | Rich test reporting                  |
| Faker          | Dynamic test data generation         |
| jsonschema     | Response schema validation           |
| python-dotenv  | Environment configuration management |
| Logging        | Request and response logging         |
| GitHub Actions | Continuous Integration (CI/CD)       |

---

## Features

* Full CRUD coverage (GET, POST, PUT, PATCH, DELETE)
* Positive and negative test scenarios
* Pagination testing
* API Client Pattern implementation
* Session reuse using `requests.Session()`
* Dynamic test data generation using Faker
* JSON Schema validation
* Structured request and response logging
* Environment configuration using `.env`
* Allure reporting with rich attachments
* Pytest markers for test categorization
* GitHub Actions CI/CD integration

---

## Project Structure

```text
api-python-framework/
│
├── api_clients/
│   ├── base_client.py
│   └── users_client.py
│
├── config/
│   └── config.py
│
├── payloads/
│   ├── create_user_payload.py
│   ├── update_user_payload.py
│   └── patch_user_payload.py
│
├── schemas/
│   └── user_schema.json
│
├── tests/
│   ├── test_users.py
│   ├── test_create_user.py
│   ├── test_update_user.py
│   ├── test_delete_user.py
│   ├── test_users_negative.py
│   └── test_users_pagination.py
│
├── utils/
│   ├── allure_helper.py
│   ├── data_generator.py
│   ├── logger.py
│   └── validator.py
│
├── reports/
│   ├── logs/
│   └── allure-results/
│
├── conftest.py
├── .env.example
├── requirements.txt
├── pytest.ini
└── README.md
```

---

## Framework Architecture

The framework follows the API Client Pattern, similar to the Page Object Model (POM) used in UI automation.

### UI Automation

```text
LoginPage
InventoryPage
CartPage
```

### API Automation

```text
AuthClient
UsersClient
ProductsClient
```

Each client is responsible for interacting with a specific group of endpoints, resulting in cleaner and more maintainable test code.

---

## Session Management

The framework uses `requests.Session()` through the `BaseClient` to:

* Reuse TCP connections
* Improve execution performance
* Centralize authentication headers
* Reduce duplicate code
* Simplify client maintenance

---

## Setup

### 1. Clone the Repository

```bash
git clone https://github.com/unaisWorks/api-python-framework.git
cd api-python-framework
```

---

### 2. Create a Virtual Environment

#### Mac/Linux

```bash
python3 -m venv venv
source venv/bin/activate
```

#### Windows

```bash
python -m venv venv
venv\Scripts\activate
```

---

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

---

### 4. Configure Environment Variables

Copy the example file:

```bash
cp .env.example .env
```

Update the values:

```env
BASE_URL=https://reqres.in/api
API_KEY=your_reqres_api_key
```

---

## Running Tests

### Run All Tests

```bash
pytest -v
```

### Run Smoke Tests

```bash
pytest -m smoke
```

### Run Regression Tests

```bash
pytest -m regression
```

### Run API Tests

```bash
pytest -m api
```

---

## Allure Reporting

Generate Allure results:

```bash
pytest --alluredir=reports/allure-results
```

Serve the report:

```bash
allure serve reports/allure-results
```

Install Allure CLI:

### Mac

```bash
brew install allure
```

### Windows

Download and install from the official Allure website.

---

## What the Allure Report Includes

* Test results grouped by feature
* Severity classifications
* Request payload attachments
* Response body attachments
* Step-level execution visibility
* Easier failure investigation

---

## CI/CD Pipeline

GitHub Actions is used to automate test execution.

Current capabilities include:

* Running tests on push events
* Running tests on pull requests
* Generating Allure results
* Uploading test artifacts
* Providing fast feedback on API quality

---

## Environment Variables

| Variable | Description            |
| -------- | ---------------------- |
| BASE_URL | Base URL of the API    |
| API_KEY  | API authentication key |

Refer to `.env.example` for configuration guidance.

---

## Key Concepts Demonstrated

This framework demonstrates:

* Building a scalable API automation framework from scratch
* Applying the API Client Pattern
* Separating concerns across clients, payloads, utilities, and tests
* Managing environments using `.env`
* Implementing schema validation
* Generating dynamic test data
* Producing actionable Allure reports
* Writing maintainable and reusable automation code
* Applying industry-standard QA automation practices

---

## Future Enhancements

Planned improvements include:

* Docker support
* Parallel execution using `pytest-xdist`
* Retry mechanisms for unstable endpoints
* OAuth 2.0 authentication flows
* Database validation
* Contract testing
* Performance testing integration

---

## Author

**Mohamed Unais**

LinkedIn:
https://www.linkedin.com/in/unaisvds/

GitHub:
https://github.com/unaisWorks

---

### About This Project

This framework represents my transition from UI Automation to API Automation as part of my journey toward becoming an industry-ready QA Automation Engineer/SDET.

It builds upon my previous experience developing Selenium frameworks with Page Object Model, Allure Reporting, Logging, GitHub, and GitHub Actions, while expanding into professional API testing practices used in modern software teams.
