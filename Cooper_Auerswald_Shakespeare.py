import string
"""
Program: Shakespeare Word Frequency Dictionary
Author: Cooper Auerswald
Course: CS2
Description:
    Reads Shakespeare plays and builds cleaned word-frequency dictionaries,
    removing stopwords, punctuation, capitalization, headers, and stage directions.
"""

INPUT_FILE_1 = "hamlet.txt"
INPUT_FILE_2 = "macbeth.txt"

OUTPUT_FILE_1 = "hamlet_word_frequency.csv"
OUTPUT_FILE_2 = "macbeth_word_frequency.csv"

TOP_WORD_LIMIT = 15

STOPWORDS = {
    "the", "and", "to", "of", "a", "in", "that", "is",
    "it", "for", "with", "as", "his", "he", "be",
    "on", "not", "by", "this", "but", "from",
    "at", "or", "an", "which", "you", "were",
    "her", "all", "she", "there", "would",
    "their", "we", "him", "been", "has",
    "had", "do", "will", "no", "if", "i", "my", "so", "what", "are",
    "me", "your", "our", "they", "them", "us", "shall", "should",
    "could", "would", "must", "may", "can", "yet", "upon", "thee", "thou"
}

def clean_word(word):
    """
    Cleans a word by converting to lowercase and removing punctuation.

    Args:
        word (str): The original word.

    Returns:
        str: The cleaned word.
    """
    return word.lower().strip(string.punctuation)

def build_dictionary(filename):
    """
    Reads a text file and builds a word frequency dictionary
    with cleaning and filtering.

    Args:
        filename (str): Path to input text file.

    Returns:
        dict: Dictionary of word -> count.
    """
    word_dict = {}

    with open(filename, "r", encoding="utf-8") as file:

        for line in file:
            # Skip empty lines
            if line.strip() == "":
                continue

            # Skip Gutenberg header/footer lines
            if line.startswith("Project Gutenberg"):
                continue

            # Skip lines that are uppercase (often scene headers, stage directions)
            if line.strip().isupper():
                continue

            words = line.split()

            for word in words:
                cleaned = clean_word(word)

                # Only count alphabetic words
                if cleaned.isalpha():

                    # Remove stopwords
                    if cleaned not in STOPWORDS:

                        # Remove very short words (<3 letters)
                        if len(cleaned) >= 3:

                            if cleaned in word_dict:
                                word_dict[cleaned] += 1
                            else:
                                word_dict[cleaned] = 1

    return word_dict

def write_to_csv(dictionary, output_filename):
    """
    Writes the top word frequencies to a CSV file.

    Args:
        dictionary (dict): word-frequency dictionary.
        output_filename (str): output CSV file path.

    Returns:
        None
    """
    # Sort by frequency descending
    sorted_words = sorted(dictionary.items(),
                          key=lambda item: item[1],
                          reverse=True)

    top_words = sorted_words[:TOP_WORD_LIMIT]

    with open(output_filename, "w", encoding="utf-8") as file:
        file.write("Word,Occurrences\n")
        for word, count in top_words:
            file.write(f"{word},{count}\n")

def main():
    """
    Main program execution.
    """
    print("Analyzing Shakespeare plays...")

    hamlet_dict = build_dictionary(INPUT_FILE_1)
    macbeth_dict = build_dictionary(INPUT_FILE_2)

    write_to_csv(hamlet_dict, OUTPUT_FILE_1)
    write_to_csv(macbeth_dict, OUTPUT_FILE_2)

    print("Analysis complete.")
    print("CSV files created and ready for Excel graphing.")


if __name__ == "__main__":
    main()
