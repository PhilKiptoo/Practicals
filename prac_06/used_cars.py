"""
CP1404/CP5632 Practical - Client code to use the Car class.
"""

from prac_06.car import Car


def main():
    """Demo test code to show how to use car class."""
    my_car = Car("Old Faithful", 180)
    my_car.drive(30)
    print(f"Car has fuel: {my_car.fuel}")
    print(my_car)

    # Create a new Car object called "limo" initialized with 100 units of fuel
    limo = Car("Limo", 100)

    # Add 20 more units of fuel to limo
    limo.add_fuel(20)

    # Print the amount of fuel in the limo
    print(f"Limo has fuel: {limo.fuel}")

    # Drive limo 115 km
    limo.drive(115)

    # Print limo to verify __str__ output
    print(limo)


main()
