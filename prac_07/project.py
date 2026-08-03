"""CP1404/CP5632 Practical - Project class."""

import datetime


class Project:
    """Represent a project with a name, start date, priority, cost and completion."""

    def __init__(self, name, start_date, priority, cost_estimate, completion_percentage):
        """Initialise a Project instance."""
        self.name = name
        self.start_date = start_date
        self.priority = priority
        self.cost_estimate = cost_estimate
        self.completion_percentage = completion_percentage

    def __str__(self):
        """Return string representation of the Project."""
        return (f"{self.name}, start: {self.start_date.strftime('%d/%m/%Y')}, "
                f"priority {self.priority}, "
                f"estimate: ${self.cost_estimate:.2f}, "
                f"completion: {self.completion_percentage}%")

    def __lt__(self, other):
        """Return True if this project has a lower (higher-importance) priority number."""
        return self.priority < other.priority

    def is_completed(self):
        """Return True if the project completion percentage is 100."""
        return self.completion_percentage == 100

    def get_start_date(self):
        """Return the project start date (used for sorting by date)."""
        return self.start_date
