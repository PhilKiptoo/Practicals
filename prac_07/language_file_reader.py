"""
CP1404/CP5632 Practical
File and class example - opens/reads a file, stores in objects of custom class.
"""

from prac_07.programming_language import ProgrammingLanguage


def main():
    """Read file of programming language details, save as objects, display."""
    languages = []
    in_file = open('prac_07/languages.csv', 'r')
    # Consume the header line
    in_file.readline()
    for line in in_file:
        parts = line.strip().split(',')
        # Convert Yes/No strings to Booleans - this is the client's job, not the class's
        reflection = parts[2] == "Yes"
        pointer_arithmetic = parts[4] == "Yes"
        language = ProgrammingLanguage(parts[0], parts[1], reflection, int(parts[3]),
                                       pointer_arithmetic)
        languages.append(language)
    in_file.close()

    for language in languages:
        print(language)


main()
