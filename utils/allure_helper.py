import json
import allure

def attach_payload(payload, name="Request Payload"):
    allure.attach(
        json.dumps(payload, indent=4),
        name=name,
        attachment_type=allure.attachment_type.JSON
    )

def attach_response(response, name="Response Body"):
    allure.attach(
        json.dumps(response.json(), indent=4),
        name=name,
        attachment_type=allure.attachment_type.JSON
    )