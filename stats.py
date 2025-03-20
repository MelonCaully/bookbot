# Returns the number of words in the text as an int
def get_num_of_words(file_text):
    word_count = 0
    for word in file_text.split():
        word_count += 1
    return word_count

def get_num_of_characters(file_text):
    char_count = {}
    for word in file_text.lower():
        if word in char_count:
            char_count[word] += 1
        else:
            char_count[word] = 1
    return char_count

def sort_dictionary(dictionary):
    sort_list = []
    for char in dictionary:
        sort_list.append({"char": char, "num": dictionary[char]})
    sort_list.sort(reverse=True, key=on_sort)
    return sort_list

def on_sort(dict):
    return dict["num"]