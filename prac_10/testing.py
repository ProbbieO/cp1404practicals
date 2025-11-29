"""
CP1404
Testing code using assert and doctest
"""

import doctest
from prac_06.car import Car


def repeat_string(s, n):
    """Repeat string s, n times, with spaces in between.
    >>> repeat_string("hi", 2)
    'hi hi'
    """
    return " ".join([s] * n)


def is_long_word(word, length=5):
    """
    Determine if the word is as long or longer than the length passed in
    >>> is_long_word("not")
    False
    >>> is_long_word("supercalifrag")
    True
    >>> is_long_word("Python", 6)
    True
    """
    return len(word) >= length


def format_as_sentence(phrase):
    """
    Format a phrase as a sentence starting with a capital and ending with a full stop.
    >>> format_as_sentence("hello")
    'Hello.'
    >>> format_as_sentence("It is an ex parrot.")
    'It is an ex parrot.'
    >>> format_as_sentence("hi there")
    'Hi there.'
    """
    phrase = phrase.strip()
    if not phrase.endswith("."):
        phrase += "."
    return phrase[0].upper() + phrase[1:]


def run_tests():
    """Run the tests on the functions."""
    # assert test with no message - used to see if the function works properly
    assert repeat_string("Python", 1) == "Python"
    # the test below should now pass
    assert repeat_string("hi", 2) == "hi hi"

    # assert test with custom message for Car odometer
    car = Car()
    assert car._odometer == 0, "Car does not set odometer correctly"

    # assert tests for Car fuel
    car = Car(fuel=10)
    assert car.fuel == 10, "Car did not set fuel correctly with custom value"

    car_default = Car()
    assert car_default.fuel == 0, "Car did not set default fuel correctly"


run_tests()

# Run doctests
doctest.testmod()
