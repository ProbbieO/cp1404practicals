"""
cp1404
prac 09
unreliableCar class
"""

from random import randint
from car import Car


class UnreliableCar(Car):
    """car that sometimes does not drive"""

    def __init__(self, name, fuel, reliability):
        """Initialise an UnreliableCar"""
        super().__init__(name, fuel)
        self.reliability = reliability

    def drive(self, distance):
        """drive on chance"""
        random_chance = randint(0, 100)
        if random_chance < self.reliability:
            # Drive normally
            return super().drive(distance)
        else:
            # Car fails to move
            return 0
