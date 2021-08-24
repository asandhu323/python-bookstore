import re


def add_book():
    """user enters book details and function adds book to list"""

    title = input("Enter book title: ")
    if re.search(r"^[0-9a-zA-Z ]+$", title) is None:
        raise ValueError("Invalid Title.")

    author = input("Enter book author: ")
    if re.search(r"^[a-zA-Z ]+$", author) is None:
        raise ValueError("Invalid Author.")

    year = input("Enter year book was released: ")
    if re.search(r"^\d{4}$", year) is None:
        raise ValueError("Invalid Year.")
    if int(year) <= 1900:
        raise ValueError("Year must be greater than 1900.")

    isbn = input("Enter book ISBN: ")
    if re.search(r"^\d{4,20}$", isbn) is None:
        raise ValueError("Invalid ISBN.")

    desc = input("Enter book description: ")
    if re.search(r"^.{1,256}$", desc) is None:
        raise ValueError("Invalid Description.")

    return {"title": title, "author": author, "year": year, "isbn": isbn, "desc": desc}


def delete_book(book_list):
    """user enters ISBN to remove book from list"""

    isbn = input("Enter ISBN of book to be deleted: ")
    if re.search(r"^\d{4,20}$", isbn) is None:
        raise ValueError("Invalid ISBN.")

    deleted = False

    for i in range(len(book_list)):
        if book_list[i]["isbn"] == isbn:
            del book_list[i]
            deleted = True
            print("Book was successfully deleted\n")
            break

    if not deleted:
        print("This book does not exist in the bookstore database.\n")

    return book_list


def book_summary(book_list):
    """displays information for each book in list"""
    for book in book_list:
        desc = book["desc"]
        desc_slice = desc[:30]
        print("Title: %s, Author: %s, Year: %s, ISBN: %s, Description: %s"
              % (book["title"], book["author"], str(book["year"]), str(book["isbn"]), desc_slice))


def search_title(book_list):
    """user enters book title and function returns matching books from list"""
    title = input("Enter book title: ")

    if re.search(r"^[0-9A-Za-z ]+$", title) is None:
        raise ValueError("Invalid Title")

    book_found = False
    for book in book_list:
        if title.lower() in book["title"].lower():
            print("Title: %s, Author: %s, Year: %s, ISBN: %s, Description: %s"
                  % (book["title"], book["author"], str(book["year"]), str(book["isbn"]), book["desc"]))
            book_found = True

    if not book_found:
        print("No matches found")


def search_author(book_list):
    """user enters book author and function returns matching books from list"""
    author = input("Enter book author: ")

    if re.search(r"^[A-Za-z ]+$", author) is None:
        raise ValueError("Invalid Author")

    book_found = False
    for book in book_list:
        if author.lower() in book["author"].lower():
            print("Title: %s, Author: %s, Year: %s, ISBN: %s, Description: %s"
                  % (book["title"], book["author"], str(book["year"]), str(book["isbn"]), book["desc"]))
            book_found = True

    if not book_found:
        print("No matches found")


def search_keyword(book_list):
    """user enters keyword and function returns matching books from list"""
    keyword = input("Enter keyword: ")

    if re.search(r"^.{1,20}$", keyword) is None:
        raise ValueError("Invalid Keyword")

    book_found = False
    for book in book_list:
        if keyword.lower() in book["title"].lower() or keyword.lower() in book["desc"].lower():
            print("Title: %s, Author: %s, Year: %s, ISBN: %s, Description: %s"
                  % (book["title"], book["author"], str(book["year"]), str(book["isbn"]), book["desc"]))
            book_found = True

    if not book_found:
        print("No matches found")
