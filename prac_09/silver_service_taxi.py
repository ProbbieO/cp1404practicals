"""
CP1404
Prac 09
SilverServiceTaxi class
"""

from taxi import Taxi


class SilverServiceTaxi(Taxi):
    """Specialised taxi """

    flagfall = 4.50

    def __init__(self, name, fuel, fanciness):
        """Initialise a SilverServiceTaxi"""
        super().__init__(name, fuel)
        self.fanciness = fanciness
        # Scale price_per_km by fanciness
        self.price_per_km *= fanciness

    def get_fare(self):
        """Return fare including flagfall"""
        base_fare = super().get_fare()
        return base_fare + self.flagfall

    def __str__(self):
        """Return string with flagfall added"""
        return f"{super().__str__()} plus flagfall of ${self.flagfall:.2f}"
