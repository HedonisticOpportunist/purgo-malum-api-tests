# -- FILE: helpers/step_helpers.py

from helpers import requests_helpers


def verify_that_status_code_is_a_match(response):
    status_code = requests_helpers.return_status_code(response=response)
    assert status_code == 200


def verify_that_the_response_contains_the_expected_boolean_value(
    response, boolean_value
):
    response_body = requests_helpers.return_json_body(response=response)
    if boolean_value == "True":
        assert response_body == True
    else:
        assert response_body == False


def verify_that_response_matches_the_given_text(response, given_text: str):
    response_body = requests_helpers.return_json_body(response=response)
    response_body_text = response_body["result"]
    assert response_body_text == given_text
