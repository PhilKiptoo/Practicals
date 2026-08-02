"""
Guitars
Estimate: 20 minutes
Actual:   15 minutes
"""

from prac_06.guitar import Guitar


def main():
    """Manage a list of user's guitars, prompting for inputs and displaying them."""
    guitars = []

    print("My guitars!")
    name = input("Name: ").strip()
    while name != "":
        year = int(input("Year: "))
        cost = float(input("Cost: $"))
        guitar_to_add = Guitar(name, year, cost)
        guitars.append(guitar_to_add)
        print(f"{guitar_to_add} added.\n")
        name = input("Name: ").strip()

    print("\nThese are my guitars:")
    for i, guitar in enumerate(guitars, 1):
        vintage_string = " (vintage)" if guitar.is_vintage() else ""
        print(f"Guitar {i}: {guitar.name:>20} ({guitar.year}), worth ${guitar.cost:10,.2f}{vintage_string}")


main()
