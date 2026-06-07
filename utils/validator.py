import json
from jsonschema import validate


def validate_json(schema_path, response_json):

    with open(schema_path, "r") as file:
        schema = json.load(file)

    validate(
        instance=response_json,
        schema=schema
    )