"""
CP1404 Assignment 1 - Books to Read
Name: Paul Omuyoma
Date Started: 22/10/25
GitHub URL:https://github.com/ProbbieO/cp1404practicals/tree/assignment1_books
"""

FILENAME = "books.csv"
UNREAD = "u"
COMPLETED = "c"


def main():
    """Main menu loop."""
    print("Books to Read 1.0 by Paul Omuyoma")
    books = load_books(FILENAME)
    print(f"{len(books)} books loaded.\n")

    choice = ""
    while choice != "Q":
        print("Menu:\nD - Display books\nA - Add a new book\nC - Complete a book\nQ - Quit")
        choice = input(">>> ").upper()
        if choice == "D":
            display_books(books)
        elif choice == "A":
            add_book(books)
        elif choice == "C":
            mark_book_completed(books)
        elif choice == "Q":
            save_books(books, FILENAME)
            print(f"{len(books)} books saved to {FILENAME}")
            print('"So many books, so little time." - Frank Zappa')
        else:
            print("Invalid menu choice")

def load_books(filename):
    """Read books from file into a list of lists."""
    books = []
    with open(filename, "r") as file:
        for line in file:
            parts = line.strip().split(",")
            parts[2] = int(parts[2])  # convert pages to int
            books.append(parts)
    return books

def save_books(books, filename):
    """Save all books back into CSV."""
    with open(filename, "w") as file:
        for book in books:
            print(f"{book[0]},{book[1]},{book[2]},{book[3]}", file=file)

def display_books(books):
    """Display books, sorted by author then title."""
    books.sort(key=lambda x: (x[1], x[0]))
    unread_books = [book for book in books if book[3] == UNREAD]
    total_pages = sum(book[2] for book in unread_books)

    for i, book in enumerate(books, 1):
        mark = "*" if book[3] == UNREAD else " "
        print(f"{mark}{i}. {book[0]:35} by {book[1]:20} {book[2]:>4} pages")

    if unread_books:
        print(f"You still need to read {total_pages} pages in {len(unread_books)} books.\n")
    else:
        print("No books left to read. Add a new book?\n")

def add_book(books):
    """Add a new book to list"""
    title = get_non_blank_input("Title: ")
    author = get_non_blank_input("Author: ")
    pages = get_positive_int("Number of Pages: ")
    books.append([title, author, pages, UNREAD])
    print(f"{title} by {author} ({pages} pages) added.\n")

def mark_book_completed(books):
    """Mark an unread book as completed"""
    unread_books = [book for book in books if book[3] == UNREAD]
    if not unread_books:
        print("No unread books - well done!\n")
        return

    display_books(books)
    number = get_valid_book_number(books)
    book = books[number - 1]
    if book[3] == COMPLETED:
        print("That book is already completed\n")
    else:
        book[3] = COMPLETED
        print(f"{book[0]} by {book[1]} completed!\n")

def get_non_blank_input(prompt):
    """Prompt until non-blank input is entered"""
    response = input(prompt).strip()
    while not response:
        print("Input can not be blank")
        response = input(prompt).strip()
    return response

def get_positive_int(prompt):
    """Prompt until valid positive integer entered"""
    while True:
        try:
            number = int(input(prompt))
            if number <= 0:
                print("Number must be > 0")
            else:
                return number
        except ValueError:
            print("Invalid input - please enter a valid number")

def get_valid_book_number(books):
    """Prompt user for book number"""
    while True:
        try:
            number = int(input("Enter the number of a book to mark as completed\n>>> "))
            if number <= 0:
                print("Number must be > 0")
            elif number > len(books):
                print("Invalid book number")
            else:
                return number
        except ValueError:
            print("Invalid input - please enter a valid number")

if __name__ == "__main__":
    main()