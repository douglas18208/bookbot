def count_words(text):
    words = text.split()
    return len(words)
# This function counts the number of words in a given text.

def count_characters(text):
    char_counts = {}
    lowered_text = text.lower()
    for char in lowered_text:
        if char in char_counts:
            char_counts[char] += 1
        else:
            char_counts[char] = 1
    # This function counts the number of characters in a given text.
    # It returns a dictionary with characters as keys and their counts as values.
        
    return char_counts

# This function counts the number of characters in a given text.

def sort_characters(char_counts):
    sorted_list = []
    for char, count in char_counts.items():
        char_data = {"character": char, "count": count}
        sorted_list.append(char_data)

    def sort_on(dict):
        return dict["count"]
    sorted_list.sort(key=sort_on, reverse=True)
    # This function sorts the character counts in descending order.
    return sorted_list

