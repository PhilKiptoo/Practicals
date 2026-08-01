"""
Wimbledon
Estimate: 30 minutes
Actual:   20 minutes
"""

FILENAME = "wimbledon.csv"


def main():
    """Read Wimbledon data, process it, and display champions and winning countries."""
    records = get_records(FILENAME)
    champion_to_count, countries = process_records(records)
    display_results(champion_to_count, countries)


def get_records(filename):
    """Get records from file as a list of lists."""
    records = []
    with open(filename, "r", encoding="utf-8-sig") as in_file:
        # Skip header line
        in_file.readline()
        for line in in_file:
            parts = line.strip().split(",")
            # Extract basic parts; index 1 and 2 are country and champion respectively
            records.append(parts)
    return records


def process_records(records):
    """Process records to find champions' win counts and set of countries."""
    champion_to_count = {}
    countries = set()
    for record in records:
        champion = record[2]
        country = record[1]
        if champion in champion_to_count:
            champion_to_count[champion] += 1
        else:
            champion_to_count[champion] = 1
        countries.add(country)
    return champion_to_count, countries


def display_results(champion_to_count, countries):
    """Display champions and sorted winning countries."""
    print("Wimbledon Champions:")
    for champion, count in champion_to_count.items():
        print(f"{champion} {count}")
    print()
    sorted_countries = sorted(list(countries))
    print(f"These {len(sorted_countries)} countries have won Wimbledon:")
    print(", ".join(sorted_countries))


main()
