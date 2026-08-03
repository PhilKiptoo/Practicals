"""CP1404/CP5632 Practical - Guitar class."""

import datetime


class Guitar:
    """Represent a Guitar object."""

    def __init__(self, name="", year=0, cost=0):
        """Initialise a Guitar instance."""
        self.name = name
        self.year = year
        self.cost = cost

    def __str__(self):
        """Return a string representation of the Guitar."""
        return f"{self.name} ({self.year}) : ${self.cost:,.2f}"

    def __lt__(self, other):
        """Return True if this guitar is older (lesser year) than the other."""
        return self.year < other.year

    def get_age(self):
        """Get the age of the guitar in years based on the current system year."""
        current_year = datetime.datetime.now().year
        return current_year - self.year

    def is_vintage(self):
        """Return True if the guitar is 50 or more years old, False otherwise."""
        return self.get_age() >= 50
