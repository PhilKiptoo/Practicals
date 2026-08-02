"""
Emails
Estimate: 20 minutes
Actual:   15 minutes
"""


def main():
    """Store user emails and names in a dictionary, checking names from emails."""
    email_to_name = {}
    email = input("Email: ").strip()
    while email != "":
        suggested_name = determine_name_from_email(email)
        confirmation = input(f"Is your name {suggested_name}? (Y/n) ").strip().lower()
        if confirmation != "" and confirmation != "y":
            name = input("Name: ").strip().title()
        else:
            name = suggested_name
        email_to_name[email] = name
        email = input("Email: ").strip()

    print()
    for email, name in email_to_name.items():
        print(f"{name} ({email})")


def determine_name_from_email(email):
    """Extract a formatted name from an email address."""
    prefix = email.split('@')[0]
    parts = prefix.split('.')
    name = " ".join(parts).title()
    return name


main()
