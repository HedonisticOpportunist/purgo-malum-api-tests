# -- FILE: /features/different_languages.feature
Feature: Contains Profanity Outlines

    Scenario Outline: As a user I want a text containing profanity is flagged as such.
        Given there is a GET request containing some <text>
        Then a 200 JSON response should be returned that flags it as <boolean_value>
        Examples:
            | text                                   | boolean_value |
            | Move bastards, you are in my way.      | True          |
            | You are fudgepacker who ate my cake    | True          |
            | I am not interested in gangbang films. | True          |
            | Honkey frotting.                       | True          |
            | Goddamnit, I lost my phone again.      | True          |
            | Do not enter this room.                | False         |

    Scenario Outline: Foreign texts should not be flagged as insults.
        Given there is a GET request containing some <phrase>
        Then a 200 JSON response should be returned that flags it as <boolean_value>
        Examples:
            | phrase   | boolean_value |
            | Japanese | False         |
            | Polish   | False         |
            | German   | False         |
            | Dutch    | False         |
            | Hindi    | False         |
            | Punjabi  | False         |




