# -- FILE: /features/different_languages.feature
Feature: Different Languages Outlines

  Scenario Outline: As a user I want to ensure that a text in a different language returns a 200 response.
    Given there is a GET request containing some text in <language>
    Then a correct <expected_response> should be returned that matches the original text
    Examples:
      | language | expected_response |
      | English  | 200               |
      | Japanese | 200               |
      | German   | 200               |
      | Hindi    | 200               |
      | Tibetian | 200               |
      | Random   | 200               |

  Scenario Outline: As a user I want to randomly select a language and have a 200 response returned.
    Given there is a GET request containing a randomly chosen text
    Then a 200 response should be returned that matches the original text





