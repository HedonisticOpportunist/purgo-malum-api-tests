# -- FILE: features/steps/different_languages.py
import logging
from pytest_bdd import scenarios as bdd_scenario, given, then, parsers
from helpers import phrase_helpers, requests
from helpers import variables

logger = logging.getLogger(__name__)
given_text = "No text provided."

bdd_scenario("../features/different_languages.feature")

""" The tests follow the ARRANGE / ACT / ASSERT PATTERN: 
https://automationpanda.com/2020/07/07/arrange-act-assert-a-pattern-for-writing-good-tests/ """


# GIVEN STEPS
@given(
    parsers.parse("there is a GET request containing some text in {language}"),
    target_fixture="select_given_language",
)
def select_given_language(language):
    # ARRANGE
    global given_text
    given_text = phrase_helpers.return_text_depending_on_language(language)


@given("there is a GET request containing a randomly chosen text")
def select_random_language():
    # ARRANGE
    global given_text
    random_language = phrase_helpers.select_random_language()
    given_text = phrase_helpers.return_text_depending_on_language(random_language)


@then(
    parsers.parse(
        "a correct {expected_response} should be returned that matches the original text"
    ),
    target_fixture="return_expected_status_code",
)
def return_expected_status_code(expected_response):

    # ACT
    response = requests.make_a_get_request(
        request_url=variables.API_JSON_TEST_ENV_URL + given_text
    )

    # ASSERT
    status_code = requests.return_status_code(response=response)
    expected_response = int(expected_response)
    assert status_code == expected_response

    response_body = requests.return_json_body(response=response)
    response_body_text = response_body["result"]
    assert response_body_text == given_text
   
@then(
    parsers.parse(
        "a 200 response should be returned that matches the original text"
    ),
    target_fixture="return_expected_status_code",
) 
def return_200_response():
    # ACT
    response = requests.make_a_get_request(
        request_url=variables.API_JSON_TEST_ENV_URL + given_text
    )

    # ASSERT
    status_code = requests.return_status_code(response=response)
    assert status_code == 200

    response_body = requests.return_json_body(response=response)
    response_body_text = response_body["result"]
    assert response_body_text == given_text
    
