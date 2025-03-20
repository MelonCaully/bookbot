import sys
from stats import *

# Returns the contents of the file as a string
def get_book_text(file_path):
    with open(file_path) as f:
        file_contents = f.read()
    return file_contents

def print_report(file, word_count, sorted_list):
    print("=========== BOOKBOT ============")
    print(f"Analyzing book found at {file}...")
    print("---------- Word Count ---------")            
    print(f"Found {word_count} total words")            
    print("------- Character Count -------")
    for item in sorted_list:
        if not item["char"].isalpha():
            continue
        print(f"{item['char']}: {item['num']}") 
               
    print("============= END ==============")
    return None

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    file = sys.argv[1]
    file_text = get_book_text(file)
    word_count = get_num_of_words(file_text)
    char_count = get_num_of_characters(file_text)
    sorted_list = sort_dictionary(char_count)
    print_report(file, word_count, sorted_list)

main()