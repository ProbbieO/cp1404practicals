"""
CP1404
Prac 09
SilverServiceTaxi
"""

from silver_service_taxi import SilverServiceTaxi

def main():
    taxi = SilverServiceTaxi("Hummer", 200, 4)
    taxi.drive(18)
    fare = taxi.get_fare()

    print(taxi)
    print(f"Fare for 18km trip = ${fare:.2f}")



main()
