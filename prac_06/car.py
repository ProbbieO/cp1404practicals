"""
CP1404
Cars class
"""

class Car:
    """Represent a Car object."""

    def __init__(self, name="", fuel=0):
        """Initialise a car instance."""
        self.name = name
        self.fuel = fuel
        self.odometer = 0

    def __str__(self):
        """Return a string representation of a car."""
        return f"{self.name}, fuel={self.fuel}, odometer={self.odometer}"

    def add_fuel(self, amount):
        """Add given amount of fuel to the car."""
        self.fuel += amount

    def drive(self, distance):
        """Drive the car a given distance if enough fuel."""
        if distance > self.fuel:
            distance = self.fuel
            self.fuel = 0
        else:
            self.fuel -= distance
        self.odometer += distance
        return distance
