"""
Practical 04 -
Quick Pick Lottery Ticket Generator
"""

import random

NUMBERS_PER_LINE = 6
MIN_NUMBER = 1
MAX_NUMBER = 45


def main():
    """get quick picks"""
    number_of_quick_picks = int(input("How many quick picks? "))

    while number_of_quick_picks <= 0:
        print("Number of picks must be greater than 0.")
        number_of_quick_picks = int(input("How many quick picks? "))

    for _ in range(number_of_quick_picks):
        quick_pick = generate_quick_pick()
        print(" ".join(f"{number:2}" for number in quick_pick))


def generate_quick_pick():
    """Generate one quick pick (list of unique random numbers)."""
    numbers = []
    while len(numbers) < NUMBERS_PER_LINE:
        number = random.randint(MIN_NUMBER, MAX_NUMBER)
        if number not in numbers:
            numbers.append(number)
    numbers.sort()
    return numbers


main()
