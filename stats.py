# Returns the number of words in the text as an int
def get_num_of_words(file_text):
    word_count = 0
    for word in file_text.split():
        word_count += 1
    return print(f"{word_count} words found in the document")

def get_num_of_characters(file_text):
    char_count = {}
    for word in file_text.lower():
        if word in char_count:
            char_count[word] += 1
        else:
            char_count[word] = 1
    return char_count

def sort_dictionary(dictionary):
    return None