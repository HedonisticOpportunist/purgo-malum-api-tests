# -- FILE: features/steps/test_contains_profanity.py
from pytest_bdd import scenarios as bdd_scenario, given, then, parsers
from helpers import requests_helpers
from helpers import step_helpers
from helpers import variables


bdd_scenario("../features/contains_profanity.feature")

""" The tests follow the ARRANGE / ACT / ASSERT PATTERN: 
https://automationpanda.com/2020/07/07/arrange-act-assert-a-pattern-for-writing-good-tests/ """

response = []


# GIVEN STEPS
@given(
    parsers.parse("there is a GET request containing some {text} with profanity"),
    target_fixture="set_up_response",
)
@given(
    parsers.parse("there is a GET request containing {text} in a foreign language"),
    target_fixture="set_up_response",
)
def set_up_response(text):
    # ARRANGE
    global response

    # ACT
    response = requests_helpers.make_a_get_request(
        request_url=variables.API_CONTAINS_PROFANITY + text
    )


@then(
    parsers.parse(
        "a 200 JSON response should be returned along with the expected {boolean_value}"
    ),
    target_fixture="determine_whether_text_contains_profanity",
)
def determine_whether_text_contains_profanity(boolean_value):

    # ASSERT
    step_helpers.verify_that_status_code_is_a_match(response=response)
    step_helpers.verify_that_the_response_contains_the_expected_boolean_value(
        response=response, boolean_value=boolean_value
    )
