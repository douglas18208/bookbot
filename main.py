from stats import *
import sys

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    book_path = sys.argv[1]




    book_words = get_book_text(book_path)
    word_count = word_counter(book_words)
    sorted_characters = character_sorter(character_counter(book_words))

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")
    print("----------- Character Count -----------")
    for item in sorted_characters:
        print(f"{item['char']}: {item['num']}")
    print("============= END ===============")




def get_book_text(book_path):
    with open(book_path) as file:
        contents = file.read()
    return contents
    
main()