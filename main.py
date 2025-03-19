from stats import *

# Returns the contents of the file as a string
def get_book_text(file_path):
    with open(file_path) as f:
        file_contents = f.read()
    return file_contents

def main():
    file_text = get_book_text("books/frankenstein.txt")
    word_count = get_num_of_words(file_text)
    char_count = get_num_of_characters(file_text)
    print(char_count)
    return None

main()