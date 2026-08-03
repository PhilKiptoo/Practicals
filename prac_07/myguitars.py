"""
My Guitars
Estimate: 25 minutes
Actual:   20 minutes
"""

from prac_07.guitar import Guitar

FILENAME = "prac_07/guitars.csv"


def main():
    """Load, display, get new guitars from user, then save back to file."""
    guitars = load_guitars(FILENAME)

    print("Guitars sorted by year:")
    guitars.sort()
    display_guitars(guitars)

    get_new_guitars(guitars)

    save_guitars(FILENAME, guitars)
    print(f"\nAll guitars saved to {FILENAME}.")


def load_guitars(filename):
    """Load guitars from CSV file and return a list of Guitar objects."""
    guitars = []
    in_file = open(filename, 'r')
    for line in in_file:
        parts = line.strip().split(',')
        guitar = Guitar(parts[0], int(parts[1]), float(parts[2]))
        guitars.append(guitar)
    in_file.close()
    return guitars


def save_guitars(filename, guitars):
    """Save list of Guitar objects to CSV file."""
    out_file = open(filename, 'w')
    for guitar in guitars:
        out_file.write(f"{guitar.name},{guitar.year},{guitar.cost}\n")
    out_file.close()


def display_guitars(guitars):
    """Display all guitars in the list."""
    for guitar in guitars:
        print(guitar)


def get_new_guitars(guitars):
    """Prompt user to add new guitars until blank name entered."""
    print("\nEnter new guitars (leave name blank to stop):")
    name = input("Name: ").strip()
    while name != "":
        year = int(input("Year: "))
        cost = float(input("Cost: $"))
        guitars.append(Guitar(name, year, cost))
        name = input("Name: ").strip()


main()
