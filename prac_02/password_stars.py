"""
Program to get a password and print.
"""

MIN_LENGTH = 5


def main():
    """Get password and print asterisks"""
    password = get_password(MIN_LENGTH)
    print_asterisks(password)


def get_password(min_length):
    """Get password"""
    password = input("Enter password: ")
    while len(password) < min_length:
        print(f"Password too short. Must be at least {min_length} characters.")
        password = input("Enter password: ")
    return password


def print_asterisks(password):
    """Print asterisks equal to the length of the password."""
    print("*" * len(password))


main()
