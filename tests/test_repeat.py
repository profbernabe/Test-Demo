from main import *


def test_repeat_multiple_times():
    assert repeat_word("hi", 3) == "hihihi"


def test_repeat_once():
    assert repeat_word("ha", 1) == "ha"


def test_repeat_longer_word():
    assert repeat_word("hello", 2) == "hellohello"

