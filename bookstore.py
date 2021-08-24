import sys
import user_actions
import file_io


def main():
    """implementation of Bookstore application"""

    if len(sys.argv) != 2:
        print("Invalid number of arguments. Enter a filename.")
        exit(0)

    filename = sys.argv[1]
    book_list = file_io.read_file(filename)

    quit_app = False

    while not quit_app:
        user_selection = input("Please select one of the following actions by pressing the corresponding key:\n"
                               "Add Book (a), Delete Book (d), View Book Summary (s), Search Book by Title (t),"
                               "Search Book by Author (u), Search Book by Keyword (k), Quit (q)\n")

        try:

            if user_selection == "a":
                book = user_actions.add_book()
                book_list.append(book)

            elif user_selection == "d":
                book_list = user_actions.delete_book(book_list)

            elif user_selection == "s":
                user_actions.book_summary(book_list)

            elif user_selection == "t":
                user_actions.search_title(book_list)

            elif user_selection == "u":
                user_actions.search_author(book_list)

            elif user_selection == "k":
                user_actions.search_keyword(book_list)

            elif user_selection == "q":
                file_io.write_file(filename, book_list)
                quit_app = True

            else:
                print("Invalid selection. Press a valid key.\n")

        except ValueError as e:
            print("ValueError: %s\n" % str(e))

    print("Thank you for using the Bookstore Application.")
    exit(0)


if __name__ == '__main__':
    main()
