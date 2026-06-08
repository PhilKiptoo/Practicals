"""
CP1404/CP5632 - Practical
Program to determine score status.
"""

import random


def main():
    """Get user score and a random score, print both results."""
    score = float(input("Enter score: "))
    result = determine_result(score)
    print(f"User score {score} is {result}")
    if result == "Excellent":
        print("You get a prize!")

    random_score = random.randint(0, 100)
    print(f"Random: {random_score} = {determine_result(random_score)}")


def determine_result(score):
    """Determine and return the status of a score."""
    if score < 0 or score > 100:
        return "Invalid score"
    elif score >= 90:
        return "Excellent"
    elif score >= 50:
        return "Passable"
    else:
        return "Bad"


if __name__ == '__main__':
    main()
