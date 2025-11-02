"""
CP1404
import code to use Car class
"""

from prac_06.car import Car

def main():
    """Demonstrate Car class usage."""
    limo = Car("Limo", 100)
    limo.add_fuel(20)
    print(f"Fuel in {limo.name}: {limo.fuel}")
    distance_driven = limo.drive(115)
    print(f"Drove {distance_driven}km")
    print(limo)

main()
