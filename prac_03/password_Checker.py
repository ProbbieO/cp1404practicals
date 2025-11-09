"""
CP1404/CP5632 Practical
Password checker program
"""

MIN_LENGTH = 8
MAX_LENGTH = 15
SPECIAL_CHARS_REQUIRED = True
SPECIAL_CHARACTERS = "!@#$%^&*()_-=+`~,./'[]<>?{}|\\"

def main():
    """Get password"""
    print("Please enter a valid password")
    print(f"Your password must be between {MIN_LENGTH} and {MAX_LENGTH} characters, and contain:")
    print("\t1 or more uppercase characters")
    print("\t1 or more lowercase characters")
    print("\t1 or more numbers")
    if SPECIAL_CHARS_REQUIRED:
        print(f"\tand 1 or more special characters:  {SPECIAL_CHARACTERS}")
    password = get_password()
    print(f"Your {len(password)} character password is valid: {password}")

def get_password():
    """Get a valid password and return it
    """
    password = input("> ")
    while not is_valid_password(password):
        print("Invalid password!")
        password = input("> ")
    return password

def is_valid_password(password):
    """Determine if password is valid"""
    if len(password) < MIN_LENGTH or len(password) > MAX_LENGTH:
        return False

    numbers_lower = numbers_upper = numbers_digit = numbers_special = 0
    for char in password:
        if char.islower():
            numbers_lower += 1
        elif char.isupper():
            numbers_upper += 1
        elif char.isdigit():
            numbers_digit += 1
        elif char in SPECIAL_CHARACTERS:
            numbers_special += 1

    if  numbers_lower == 0 or numbers_upper == 0 or numbers_digit == 0:
        return False
    if SPECIAL_CHARS_REQUIRED and numbers_special == 0:
        return False
    return True

main()
