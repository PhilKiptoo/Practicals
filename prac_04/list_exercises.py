"""
CP1404/CP5632 Practical
List exercises: basic list operations and a username security checker.
"""


def main():
    """Run basic list exercises and the security checker."""
    # Part 1: Basic list operations
    numbers = []
    for _ in range(5):
        number = float(input("Number: "))
        # Convert to integer if it has no fractional part for cleaner output
        if number.is_integer():
            number = int(number)
        numbers.append(number)

    print(f"The first number is {numbers[0]}")
    print(f"The last number is {numbers[-1]}")
    print(f"The smallest number is {min(numbers)}")
    print(f"The largest number is {max(numbers)}")
    print(f"The average of the numbers is {sum(numbers) / len(numbers):.1f}")

    print()  # Spacer line

    # Part 2: Username security checker
    usernames = ['jimbo', 'giltson98', 'derekf', 'WhatSup', 'NicolEye', 'swei45',
                 'BaseInterpreterInterface', 'BaseStdIn', 'Command', 'ExecState',
                 'InteractiveConsole', 'InterpreterInterface', 'StartServer', 'bob']

    username = input("Enter username: ")
    if username in usernames:
        print("Access granted")
    else:
        print("Access denied")


if __name__ == '__main__':
    main()
