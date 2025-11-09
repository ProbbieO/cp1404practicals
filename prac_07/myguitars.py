"""
CP1404
Guitar objects program - read, display, sort, add, and save guitars
"""

from guitar import Guitar


def main():
    """Read guitars from file, sort, display, get user input, and save."""
    guitars = load_guitars("guitars.csv")
    print_guitars(guitars)

    guitars.sort()
    print("\nSorted by year:")
    print_guitars(guitars)

    add_new_guitars(guitars)
    save_guitars("guitars.csv", guitars)


def load_guitars(filename):
    """Load guitars from a CSV file."""
    guitars = []
    in_file = open(filename, 'r')

    for line in in_file:
        parts = line.strip().split(',')
        guitar = Guitar(parts[0], int(parts[1]), float(parts[2]))
        guitars.append(guitar)

    in_file.close()
    return guitars


def print_guitars(guitars):
    """Display guitars from the list."""
    for guitar in guitars:
        print(guitar)


def add_new_guitars(guitars):
    """Allow user to add new guitars."""
    print("\nAdd new guitars (blank name to finish)")
    name = input("Name: ")
    while name != "":
        year = int(input("Year: "))
        cost = float(input("Cost: $"))
        guitars.append(Guitar(name, year, cost))
        print(f"{name} added.")
        name = input("Name: ")


def save_guitars(filename, guitars):
    """Save guitars to CSV file."""
    out_file = open(filename, 'w')
    for guitar in guitars:
        out_file.write(f"{guitar.name},{guitar.year},{guitar.cost}\n")
    out_file.close()
    print("\nGuitars saved to file.")


if __name__ == "__main__":
    main()
