"""
Program to get a password with error-checking and print stars as long as the password.
"""

MIN_LENGTH = 5


def main():
    """Get password and print asterisks for its length."""
    password = get_password(MIN_LENGTH)
    print_asterisks(password)


def get_password(min_length):
    """Get a valid password with at least min_length characters."""
    password = input("Enter password: ")
    while len(password) < min_length:
        print(f"Password too short. Must be at least {min_length} characters.")
        password = input("Enter password: ")
    return password


def print_asterisks(password):
    """Print asterisks equal to the length of the password."""
    print("*" * len(password))


main()
