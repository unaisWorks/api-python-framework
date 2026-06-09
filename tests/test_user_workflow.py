import allure
import json
import pytest

@pytest.mark.api
@pytest.mark.regression
@allure.title("Create Update Delete User Workflow")
def test_user_workflow(client):

    #create User
    create_payload = {
        "name" : "sam",
        "job" : "QA"
    }
    allure.attach(
        json.dumps(create_payload, indent=4),
        name="Create User Payload",
        attachment_type=allure.attachment_type.JSON
    )

    create_response = client.create_user(create_payload)

    allure.attach(
        json.dumps(create_response.json(), indent=4),
        name="Create User Response",
        attachment_type=allure.attachment_type.JSON
    )

    assert create_response.status_code == 201

    user_id = create_response.json()["id"]

    client.logger.info(f"Created User ID: {user_id}")

    allure.attach(
        str(user_id),
        name="Generated User ID"
    )

    assert create_response.json()["name"] == create_payload["name"]

    #update user
    update_payload = {
        "name" : "Sam Updated",
        "job" : "QA Lead"
    }

    allure.attach(
        json.dumps(update_payload, indent=4),
        name="Update User Payload",
        attachment_type=allure.attachment_type.JSON
    )

    update_response = client.update_user(user_id,update_payload)

    allure.attach(
        json.dumps(update_response.json(), indent=4),
        name="Update User Response",
        attachment_type=allure.attachment_type.JSON
    )

    assert update_response.status_code == 200
    assert update_response.json()["name"] == update_payload["name"]

    #Delete Same User
    delete_response = client.delete_user(user_id)

    assert delete_response.status_code ==204

    allure.attach(
        str(delete_response.status_code),
        name="Delete User Status"
    )


