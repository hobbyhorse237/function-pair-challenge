from lib.function_pair_challenge import *


def test_if_no_keyword_returns_false():
    assert check_for_todo("Release the cat.") == False

def test_if_keyword_returns_true():
    assert check_for_todo("Release the cat #TODO.") == True

def test_if_given_empty_string():
    assert check_for_todo("") == False