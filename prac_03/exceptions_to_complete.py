"""
CP1404/CP5632 Practical
Program to get and validate integer input using exception handling
"""

is_finished = False
result = 0
while not is_finished:
    try:
        number = int(input("Enter a valid integer: "))
        finished = True
    except ValueError:
        print("Please enter a valid integer.")
print(f"Valid result is: {number}")
