"""
Practical 05
State names
"""

STATE_NAMES = {
    "QLD": "Queensland",
    "NSW": "New South Wales",
    "NT": "Northern Territory",
    "WA": "Western Australia",
    "ACT": "Australian Capital Territory",
    "VIC": "Victoria",
    "TAS": "Tasmania"
}

def main():
    """Look up state abbreviations and print their full names."""
    state_code = input("Enter short state: ").strip().upper()
    while state_code != "":
        try:
            print(f"{state_code} is {STATE_NAMES[state_code]}")
        except KeyError:
            print("Invalid short state")
        state_code = input("Enter short state: ").strip().upper()

    print("\nAll states and names:")
    for code, name in STATE_NAMES.items():
        print(f"{code:3} is {name}")

main()
