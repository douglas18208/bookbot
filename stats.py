def word_counter(book_words):
    words = book_words.split()
    return len(words)

def character_counter(book_words):
    char_count = {}
    lower_words = book_words.lower()
    for char in lower_words:
        if char.isalpha():
            if char in char_count:
                char_count[char] += 1
            else:
                char_count[char] = 1
    return char_count

def character_sorter(char_count):
    sorted_char = []
    for char in char_count:
        count = char_count[char]
        single_char = {"char": char, "num": count}  
        sorted_char.append(single_char)
    
    def sort_by_num(single_char):
        return single_char["num"]
    sorted_char.sort(key=sort_by_num, reverse=True)
    return sorted_char