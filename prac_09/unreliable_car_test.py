"""
CP1404
Prac 09
UnreliableCar
"""

from unreliable_car import UnreliableCar

def main():
    """Test UnreliableCar function"""

    car = UnreliableCar("Half Reliable", 100, 50)

    for i in range(10):
        distance_tried = 10
        distance_driven = car.drive(distance_tried)
        print(f"Attempt {i+1}: tried to drive {distance_tried}km, actually drove {distance_driven}km")

main()
