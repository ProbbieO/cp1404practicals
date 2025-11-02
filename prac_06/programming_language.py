"""
CP1404
Programming Language class
"""

class ProgrammingLanguage:
    """Represent information about a programming language."""

    def __init__(self, name, typing, reflection, year):
        self.name = name
        self.typing = typing
        self.reflection = reflection
        self.year = year

    def is_dynamic(self):
        """Return if language is dynamically typed."""
        return self.typing.lower() == "dynamic"

    def __str__(self):
        """Return string of ProgrammingLanguages."""
        return f"{self.name}, {self.typing} Typing, Reflection={self.reflection}, First appeared in {self.year}"
