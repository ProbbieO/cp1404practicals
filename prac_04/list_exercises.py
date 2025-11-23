"""
Practical 04 - Lists
"""

# 1 Lists


def main():
    """Main function to run"""
    numbers = get_numbers()
    display_number_info(numbers)
    check_access()


def get_numbers():
    """Prompt the user for 5 numbers and store them in a list."""
    numbers = []
    for i in range(5):
        number = int(input("Number: "))
        numbers.append(number)
    return numbers


def display_number_info(numbers):
    """Display basic information about the numbers."""
    print(f"The first number is {numbers[0]}")
    print(f"The last number is {numbers[-1]}")
    print(f"The smallest number is {min(numbers)}")
    print(f"The largest number is {max(numbers)}")
    print(f"The average of the numbers is {sum(numbers) / len(numbers):.1f}")

# 2 Security checker

def check_access():
    """Check if a username is authorised."""
    usernames = [
        'jimbo', 'giltson98', 'derekf', 'WhatSup', 'NicolEye',
        'swei45', 'BaseInterpreterInterface', 'BaseStdIn',
        'Command', 'ExecState', 'InteractiveConsole',
        'InterpreterInterface', 'StartServer', 'bob'
    ]

    username = input("Username: ")
    if username in usernames:
        print("Access granted")
    else:
        print("Access denied")

main()
