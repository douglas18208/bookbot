from stats import *

def main():
    book_words = get_book_text("books/frankenstein.txt")
    word_count = word_counter(book_words)
    print(f"{word_count} words found in the document")
    print(character_counter(book_words))



def get_book_text(book_path):
    with open(book_path) as file:
        contents = file.read()
    return contents
    
main()