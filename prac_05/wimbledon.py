"""
Wimbledon data reading, processing and displaying
"""


def main():
    """Display Wimbledon champions and countries"""
    filename = "wimbledon.csv"
    records = load_data(filename)
    champion_to_wins = count_champions(records)
    countries = extract_countries(records)
    display_results(champion_to_wins, countries)


def load_data(filename):
    """Read Wimbledon data from CSV file into a list of lists"""
    records = []
    with open(filename, "r", encoding="utf-8-sig") as in_file:
        in_file.readline()  # skip header line
        for line in in_file:
            parts = line.strip().split(",")
            records.append(parts)
    return records


def count_champions(records):
    """Count how many times each champion has won"""
    champion_to_wins = {}
    for record in records:
        champion = record[2]
        champion_to_wins[champion] = champion_to_wins.get(champion, 0) + 1
    return champion_to_wins


def extract_countries(records):
    """Extract a set of unique countries from data"""
    countries = {record[1] for record in records}
    return countries


def display_results(champion_to_wins, countries):
    """Display champions and countries"""
    print("Wimbledon Champions:")
    for champion, wins in champion_to_wins.items():
        print(f"{champion:20} : {wins}")

    print(f"\nThese {len(countries)} countries have won Wimbledon:")
    print(", ".join(sorted(countries)))


main()
