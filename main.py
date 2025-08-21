from stats import get_word_count
from stats import get_letter_count
from stats import report
import sys

def get_book_text(filepath):
    with open(filepath) as f:
        file_content = f.read()
        return file_content 

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
        return
    content = get_book_text(sys.argv[1])
    num_words = get_word_count(content)
    letter_count = get_letter_count(content)
    letter_list = report(letter_count)
    idk =[]
    for my_dict in letter_list:
        idk.append(f"{my_dict["char"]}: {my_dict["num"]}")
    letter_list_count = "\n".join(idk)
    
    print(f"""============ BOOKBOT ============
    Analyzing book found at {sys.argv[1]}...
    ----------- Word Count ----------
    Found {num_words} total words
    --------- Character Count -------
    {letter_list_count} 
    ============= END ===============""")

main()



