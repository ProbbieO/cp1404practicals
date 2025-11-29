"""
CP1404
Prac 09
Taxi Simulator
"""

from taxi import Taxi
from silver_service_taxi import SilverServiceTaxi


def main():
    """Taxi simulator"""
    print("Let's drive!")
    taxis = [
        Taxi("Prius", 100),
        SilverServiceTaxi("Limo", 100, 2),
        SilverServiceTaxi("Hummer", 200, 4)
    ]
    current_taxi = None
    bill_to_date = 0

    menu = "q)uit, c)hoose taxi, d)rive"
    print(menu)
    choice = input(">>> ").lower()

    while choice != "q":
        if choice == "c":
            # Choose taxi
            current_taxi = choose_taxi(taxis)
        elif choice == "d":
            # Drive taxi
            if current_taxi is None:
                print("You need to choose a taxi before you can drive")
            else:
                trip_cost = drive_taxi(current_taxi)
                bill_to_date += trip_cost
        else:
            print("Invalid option")

        print(f"Bill to date: ${bill_to_date:.2f}")
        print(menu)
        choice = input(">>> ").lower()


    print(f"Total trip cost: ${bill_to_date:.2f}")
    print("Taxis are now:")
    display_taxis(taxis)


def choose_taxi(taxis):
    """display taxis and return the chosen taxi object"""
    print("Taxis available:")
    display_taxis(taxis)

    try:
        taxi_choice = int(input("Choose taxi: "))
        if 0 <= taxi_choice < len(taxis):
            return taxis[taxi_choice]
        else:
            print("Invalid taxi choice")
            return None
    except ValueError:
        print("Invalid input")
        return None


def drive_taxi(taxi):
    """Drive the chosen taxi and return the cost."""
    try:
        distance = float(input("Drive how far? "))
    except ValueError:
        print("Invalid distance")
        return 0

    taxi.start_fare()
    taxi.drive(distance)
    fare = taxi.get_fare()
    print(f"Your {taxi.name} trip cost you ${fare:.2f}")
    return fare


def display_taxis(taxis):
    """display list of taxis"""
    for i, taxi in enumerate(taxis):
        print(f"{i} - {taxi}")



main()
