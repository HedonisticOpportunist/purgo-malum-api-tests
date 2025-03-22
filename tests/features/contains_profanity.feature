# -- FILE: /features/contains_profanity.feature
Feature: Contains Profanity Outlines

    Scenario Outline: As a user, I want a text containing profanity to be flagged as insults.
        Given there is a GET request containing some <text> with profanity
        Then a 200 JSON response should be returned along with the expected <boolean_value>
        Examples:
            | text                                   | boolean_value |
            | Move bastards, you are in my way.      | True          |
            | You are fudgepacker who ate my cake    | True          |
            | I am not interested in gangbang films. | True          |
            | Honkey frotting.                       | True          |
            | Goddamnit, I lost my phone again.      | True          |
            | Do not enter this room.                | False         |

    Scenario Outline: As a user, I do not expect foreign texts containing insults to be flagged (as the application focuses on the English language).
        Given there is a GET request containing some <text> in a foreign language
        Then a 200 JSON response should be returned along with the expected <boolean_value>
        Examples:
            | text     | boolean_value |
            | Japanese | False         |
            | Polish   | False         |
            | German   | False         |
            | Dutch    | False         |
            | Hindi    | False         |
            | Punjabi  | False         |




