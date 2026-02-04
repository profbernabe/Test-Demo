from main import *

def test_add_positive_numbers():
    assert add(1, 2) == 3


def test_add_with_zero():
    assert add(1, 0) == 1


def test_add_negative_number():
    assert add(2, -3) == -1


def test_add_two_negatives():
    assert add(-2, -5) == -7
