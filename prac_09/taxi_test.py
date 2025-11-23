"""
CP1404
Prac 09
Taxi test
"""

from taxi import Taxi

def main():
    """Test the Taxi class."""
    # create taxi
    my_taxi = Taxi("Prius 1", 100)

    # drive 40km
    my_taxi.drive(40)

    # print taxi & fare
    print(my_taxi)
    print(f"Current fare: ${my_taxi.get_fare():.2f}")

    # start new fare & drive 100km
    my_taxi.start_fare()
    my_taxi.drive(100)


    print(my_taxi)
    print(f"Current fare: ${my_taxi.get_fare():.2f}")


main()
