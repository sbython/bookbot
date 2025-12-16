from stats import get_num_char, get_num_words
import sys

arg = sys.argv
if len(arg) != 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)

PATH = arg[1]
def get_book_text(PATH):
    contents = ""
    with open(PATH) as df:
        contents = df.read()
    return contents


def main():
    contents = get_book_text(PATH)
    num_of_word = get_num_words(contents)
    dic = get_num_char(contents)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {PATH}...")
    print("----------- Word Count ----------")
    print(f"Found {num_of_word} total words")
    print("--------- Character Count -------")
    for i in dic:
        print(f"{i['char']}: {i['num']}")
    print("============= END ===============")

main()
