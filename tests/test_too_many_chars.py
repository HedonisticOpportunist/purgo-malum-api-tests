# -- FILE: tests/test_too_many_chars.py
from pytest_bdd import scenarios as bdd_scenario, given, then, parsers
from helpers import requests_helpers, step_helpers
from helpers import variables
import xmltodict


response = []

bdd_scenario("../features/too_many_chars.feature")

""" The tests follow the ARRANGE / ACT / ASSERT PATTERN: 
https://automationpanda.com/2020/07/07/arrange-act-assert-a-pattern-for-writing-good-tests/ """


# GIVEN STEPS
@given(
    parsers.parse("there is a GET request containing some {text}"),
    target_fixture="set_up_error_response",
)
def set_up_error_response(text):
    # ARRANGE
    global response

    # ACT
    response = requests_helpers.make_a_get_request(
        request_url=variables.API_ERROR_PATH + text
    )


@then(
    parsers.parse("a response should be returned that marks it as an error"),
)
def return_200_response_with_error():

    # ASSERT
    step_helpers.verify_that_status_code_is_a_match(response=response)

    # Returns not well-formed error
    # dict_data = xmltodict.parse(response.content)
    # dict_data
