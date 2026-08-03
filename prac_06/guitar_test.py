"""
CP1404/CP5632 Practical - Test code for the Guitar class.
"""

from prac_06.guitar import Guitar


def main():
    """Test methods in Guitar class."""
    gibson = Guitar("Gibson L-5 CES", 1922, 16035.40)
    another = Guitar("Another Guitar", 2013, 1000)

    # Test get_age() - expected values are literals (hardcoded), not computed
    print(f"{gibson.name} get_age() - Expected 104. Got {gibson.get_age()}")
    print(f"{another.name} get_age() - Expected 13. Got {another.get_age()}")

    # Test is_vintage()
    print(f"{gibson.name} is_vintage() - Expected True. Got {gibson.is_vintage()}")
    print(f"{another.name} is_vintage() - Expected False. Got {another.is_vintage()}")


main()
