# -- FILE: features/steps/different_languages.py
import logging
from pytest_bdd import scenarios as bdd_scenario, given, then, parsers
from helpers import requests
from helpers import variables

logger = logging.getLogger(__name__)
given_text = "No text provided."

bdd_scenario("../features/contains_profanity.feature")

""" The tests follow the ARRANGE / ACT / ASSERT PATTERN: 
https://automationpanda.com/2020/07/07/arrange-act-assert-a-pattern-for-writing-good-tests/ """

provided_text = ""


# GIVEN STEPS
@given(
    parsers.parse("there is a GET request containing some {text}"),
    target_fixture="deal_with_text",
)
def deal_with_text(text):
    # ARRANGE
    global provided_text
    provided_text = text


@given(
    parsers.parse("there is a GET request containing some {phrase}"),
    target_fixture="deal_with_foreign_text_containing_insults",
)
def deal_with_foreign_text_containing_insults(phrase):
    # ARRANGE
    global provided_text
    provided_text = phrase


@then(
    parsers.parse(
        "a 200 JSON response should be returned that flags it as {boolean_value}"),
        target_fixture="flag_as_profanity",
    )

def flag_as_profanity(boolean_value):

    # ACT
    global provided_text
    response = requests.make_a_get_request(
        request_url=variables.API_CONTAINS_PROFANITY + provided_text
    )

    # ASSERT
    status_code = requests.return_status_code(response=response)
    assert status_code == 200
    response_body = requests.return_json_body(response=response)

    if boolean_value == "True":
        assert response_body == True
    else:
        assert response_body == False
