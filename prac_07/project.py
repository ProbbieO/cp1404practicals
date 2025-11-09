"""
CP1404
Project class for Project Management program
"""

import datetime


class Project:
    """Represent a project with name, start date, priority, cost and completion."""

    def __init__(self, name, start_date, priority, cost_estimate, completion_percent):
        """Initialise a Project instance."""
        self.name = name
        self.start_date = start_date  # datetime.date
        self.priority = priority
        self.cost_estimate = cost_estimate
        self.completion_percent = completion_percent

    def __str__(self):
        """Return string representation of a Project."""
        return f"{self.name}, start: {self.start_date.strftime('%d/%m/%Y')}, " \
               f"priority {self.priority}, estimate: ${self.cost_estimate:.2f}, " \
               f"completion: {self.completion_percent}%"

    def __lt__(self, other):
        """Sort projects by priority."""
        return self.priority < other.priority

    def is_complete(self):
        """Return True if project is 100% complete."""
        return self.completion_percent == 100
