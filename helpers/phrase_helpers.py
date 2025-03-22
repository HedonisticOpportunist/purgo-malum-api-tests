# -- FILE: helpers/phrase_helpers.py

import random


def return_text_depending_on_language(language: str):
    selected_language = language.lower()
    text_str = ""
    if selected_language == "japanese":
        text_str = "これは日本語のテキストです."
    if selected_language == "english":
        text_str = "This is a Japanese text."
    if selected_language == "german":
        text_str = "Dies ist ein japanischer Text."
    if selected_language == "tibetian":
        text_str = "དི་ཉི་ཧོང་གི་ཡི་གེ་རེད།"
    if selected_language == "hindi":
        text_str = "यह एक जापानी पाठ है."
    else:
        text_str = "No language provided."
    return text_str


def select_random_language():
    languages = ["German", "Tibetian", "French", "Japanese"]
    return random.choice(languages)


def select_phrase(selected_phrase: str):
    chosen_phrase = selected_phrase.lower()
    phrase_str = ""
    if chosen_phrase == "japanese":
        phrase_str = "泣けよ、バカ野郎"
    if chosen_phrase == "polish":
        "placz, dupku"
    if chosen_phrase == "german":
        phrase_str = "heule du Arschloch"
    if chosen_phrase == "dutch":
        phrase_str = "huil maar, klootzak"
    if chosen_phrase == "hindi":
        phrase_str = "रोओ तुम गधे"
    if chosen_phrase == "punjabi":
        phrase_str = "ਰੋਵੋ ਗਧੇ"
    else:
        phrase_str = "No insult provided."
    return phrase_str
