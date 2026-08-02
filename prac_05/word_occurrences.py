"""
Word Occurrences
Estimate: 15 minutes
Actual:   10 minutes
"""


def main():
    """Count occurrences of words in a string and print sorted, aligned results."""
    text = input("Text: ")
    words = text.split()

    # Count word frequencies
    word_to_count = {}
    for word in words:
        if word in word_to_count:
            word_to_count[word] += 1
        else:
            word_to_count[word] = 1

    # Sort words alphabetically
    sorted_words = sorted(word_to_count.keys())

    # Find the length of the longest word for alignment
    longest_word_length = 0
    for word in sorted_words:
        if len(word) > longest_word_length:
            longest_word_length = len(word)

    # Print formatted output
    for word in sorted_words:
        print(f"{word:{longest_word_length}} : {word_to_count[word]}")


main()
