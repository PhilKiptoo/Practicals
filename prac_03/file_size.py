"""
CP1404/CP5632 - Practical
Program to count the number of lines in a file.
"""


def main():
    """Keep asking for filenames and printing their line counts until empty string."""
    filename = input("Enter filename: ")
    while filename != "":
        try:
            line_count = count_lines_in_file(filename)
            print(f"{filename} has {line_count} lines.")
        except FileNotFoundError:
            print(f"ERROR: {filename} does not exist.")
        filename = input("Enter filename: ")


def count_lines_in_file(filename):
    """Count and return the number of lines in a file. Do not catch exceptions here."""
    with open(filename, 'r', encoding='utf-8') as in_file:
        line_count = len(in_file.readlines())
    return line_count


if __name__ == '__main__':
    main()
