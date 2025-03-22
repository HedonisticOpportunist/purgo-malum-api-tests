# -- FILE: /features/too_many_chars.feature
Feature: Contains Too Many Characters Outlines

    Scenario Outline: As a user, I want a text that is too long to return an error.
        Given there is a GET request containing some <text>
        Then a response should be returned that marks it as an error
        Examples:
            | text                                                             |
            | An elephant never forgets. This means you should never hurt one. |
            | A long time ago, I used to believe in dreams.                    |
            | There, there. You will get over it.                              |






