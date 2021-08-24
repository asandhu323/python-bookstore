import json
import os


def read_file(filename):
    """takes filename and reads books from file and returns list of books"""

    if os.path.isfile(filename):
        book_file = open(filename)
        book_data = book_file.read()
        book_file.close()

        book_list = json.loads(book_data)

    else:
        print("The bookstore database does not exist.\n")
        book_list = []

    return book_list


def write_file(filename, book_list):
    """takes in list of books and writes them to file in json format"""

    book_file = open(filename, "w")
    book_json = json.dumps(book_list, indent=4)
    book_file.write(book_json)
    book_file.close()
