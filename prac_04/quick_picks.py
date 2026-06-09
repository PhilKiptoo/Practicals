"""
CP1404/CP5632 Practical
"Quick Pick" Lottery Ticket Generator
"""

import random

NUMBERS_PER_LINE = 6
MIN_NUMBER = 1
MAX_NUMBER = 45


def main():
    """Generate a requested number of quick pick lines with unique sorted random numbers."""
    number_of_quick_picks = int(input("How many quick picks? "))
    while number_of_quick_picks < 0:
        print("Invalid number of quick picks!")
        number_of_quick_picks = int(input("How many quick picks? "))

    for _ in range(number_of_quick_picks):
        quick_pick = []
        while len(quick_pick) < NUMBERS_PER_LINE:
            number = random.randint(MIN_NUMBER, MAX_NUMBER)
            if number not in quick_pick:
                quick_pick.append(number)
        quick_pick.sort()
        print(" ".join(f"{number:2}" for number in quick_pick))


if __name__ == '__main__':
    main()
