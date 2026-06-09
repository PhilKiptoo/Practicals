"""
CP1404/CP5632 Practical
Data file -> lists program
"""

FILENAME = "subject_data.txt"


def main():
    """Program to load and display subject details from a file."""
    subject_records = load_subject_records(FILENAME)
    display_subject_records(subject_records)


def load_subject_records(filename=FILENAME):
    """Read data from file formatted like: subject,lecturer,number of students."""
    subject_records = []
    with open(filename, 'r', encoding='utf-8') as input_file:
        for line in input_file:
            line = line.strip()
            parts = line.split(',')
            parts[2] = int(parts[2])  # Convert student count to integer
            subject_records.append(parts)
    return subject_records


def display_subject_records(subject_records):
    """Display subject details formatted nicely in columns."""
    for record in subject_records:
        subject_code, lecturer, number_of_students = record
        print(f"{subject_code} is taught by {lecturer:<12} and has {number_of_students:>3} students")


if __name__ == '__main__':
    main()
