"""
Practical 5
Word Occurrences

"""

def main():
    """Count word occurrences in a line of text"""
    text = input("Text: ")
    words = text.split()
    word_to_count = {}

    for word in words:
        # Convert all to lowercase
        word = word.lower()
        if word in word_to_count:
            word_to_count[word] += 1
        else:
            word_to_count[word] = 1

    # Sort words alphabetically
    sort_words = sorted(word_to_count.keys())

    # Find longest word for formatting
    max_length = max(len(word) for word in sort_words)

    # Display neatly aligned output
    for word in sort_words:
        print(f"{word:{max_length}} : {word_to_count[word]}")

main()
