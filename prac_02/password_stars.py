"""
CP1404/CP5632 - Practical
Password check program with stars output.
"""

MINIMUM_LENGTH = 6


def main():
    """Drive the password check and stars display."""
    password = get_password()
    print_stars(password)


def get_password():
    """Get and return a valid password of at least MINIMUM_LENGTH characters."""
    password = input("Enter password: ")
    while len(password) < MINIMUM_LENGTH:
        print(f"Password must be at least {MINIMUM_LENGTH} characters")
        password = input("Enter password: ")
    return password


def print_stars(password):
    """Print one asterisk for each character in password."""
    print('*' * len(password))


if __name__ == '__main__':
    main()
