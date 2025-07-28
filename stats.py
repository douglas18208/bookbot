def word_counter(book_words):
    words = book_words.split()
    return len(words)

def character_counter(book_words):
    char_count = {}
    lower_words = book_words.lower()
    for char in lower_words:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
    return char_count
