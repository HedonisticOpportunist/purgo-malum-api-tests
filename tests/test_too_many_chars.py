# -- FILE: features/steps/different_languages.py
import logging
from pytest_bdd import scenarios as bdd_scenario, given, then, parsers
from helpers import requests
from helpers import variables
import xmltodict

logger = logging.getLogger(__name__)
given_text = "this is curiously long replacement text"

bdd_scenario("../features/too_many_chars.feature")

""" The tests follow the ARRANGE / ACT / ASSERT PATTERN: 
https://automationpanda.com/2020/07/07/arrange-act-assert-a-pattern-for-writing-good-tests/ """


# GIVEN STEPS
@given(
    parsers.parse("there is a GET request containing some {long_text}"),
    target_fixture="select_given_language",
)
def deal_with_long_text(long_text):
    # ARRANGE
    global given_text
    given_text = long_text


@then(
    parsers.parse("a response should be returned that marks it as an error"),
)
def return_200_response_with_error():
    # ACT
    response = requests.make_a_get_request(
        request_url=variables.API_JSON_TEST_ENV_URL + given_text
    )

    # ASSERT
    status_code = requests.return_status_code(response=response)
    assert status_code == 200

    # Returns not well-formed error
    # dict_data = xmltodict.parse(response.content)
    # dict_data
