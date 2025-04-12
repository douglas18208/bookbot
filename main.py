import sys
if len(sys.argv) != 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)


def get_book_text(filepath):
    with open(filepath) as f:
        return f.read()
# This function reads the content of a book file and returns it as a string.


from stats import count_words
from stats import count_characters
from stats import sort_characters

def main():
    book_path = sys.argv[1]
    book_text = get_book_text(book_path)
    word_count = count_words(book_text)
    char_count = count_characters(book_text)
    sorted_char_count = sort_characters(char_count)
    
    # Print report header
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    
    # Print word count section
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")
    
    # Print character count section
    print("--------- Character Count -------")
    
    # Only print alphabetical characters
    for char_data in sorted_char_count:
        char = char_data["character"]
        count = char_data["count"]
        
        # This is where we use isalpha() to filter
        if char.isalpha():
            print(f"{char}: {count}")
    
    # Print footer
    print("============= END ===============")

main()