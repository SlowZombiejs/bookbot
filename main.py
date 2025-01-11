def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    chars_dict = get_characters_count(text)
    print(f"--- Begin report of books/frankenstein.txt ---\n{num_words} words found in the document\n ")
    # Sort characters by occurrence and print them
    sorted_characters = sort_characters_by_occurrence(chars_dict)
    for char, count in sorted_characters:
        if char.isalpha():  # Only print printable characters
            print(f"The '{char}' character was found {count} times")

def get_book_text(path):
    with open(path) as f:
        return f.read()

def get_num_words(text):
    words = text.split()
    return len(words)

def get_characters_count(text):
    characters = {}
    for c in text:
        lowered = c.lower()
        if lowered in characters:
            characters[lowered] += 1
        else:
            characters[lowered] = 1
    return characters
    
def sort_characters_by_occurrence(characters):
    # Convert dictionary to a list of tuples and sort by count in descending order
    return sorted(characters.items(), key=lambda item: item[1], reverse=True)


if __name__ == "__main__":
    main()