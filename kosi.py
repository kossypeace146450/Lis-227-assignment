class Book:
    def __init__(self, title, author, isbn):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.is_borrowed = False

class JohnHarrisLibrary:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)

    def display_books(self):
        print("Books in the John Harris Library:")
        for index, book in enumerate(self.books, start=1):
            status = "Borrowed" if book.is_borrowed else "Available"
            print(f"{index}. Title: {book.title}, Author: {book.author}, ISBN: {book.isbn}, Status: {status}")

    def view_authors(self):
        authors = set(book.author for book in self.books)
        print("Authors in the John Harris Library:")
        for author in authors:
            print(author)

    def view_inventory(self):
        print("Complete Inventory of the John Harris Library:")
        for index, book in enumerate(self.books, start=1):
            status = "Borrowed" if book.is_borrowed else "Available"
            print(f"{index}. Title: {book.title}, Author: {book.author}, ISBN: {book.isbn}, Status: {status}")

    def borrow_book(self, book_index):
        if 0 < book_index <= len(self.books):
            book = self.books[book_index - 1]
            if not book.is_borrowed:
                book.is_borrowed = True
                print(f"You have borrowed '{book.title}'. Enjoy your reading!")
            else:
                print(f"'{book.title}' is already borrowed.")
        else:
            print("Invalid book index.")

def main():
    john_harris_library = JohnHarrisLibrary()

    # Sample poetry books
    sample_books = [
        Book("The Waste Land", "T.S. Eliot", "9780156634550"),
        Book("Leaves of Grass", "Walt Whitman", "9780486419304"),
        Book("The Raven and Other Poems", "Edgar Allan Poe", "9780486280486")
        # Add more sample books if needed
    ]

    for book in sample_books:
        john_harris_library.add_book(book)

    while True:
        print("John Harris Library Management System")
        print("1. Display Books")
        print("2. View Authors")
        print("3. View Inventory")
        print("4. Borrow Book")
        print("0. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            john_harris_library.display_books()

        elif choice == '2':
            john_harris_library.view_authors()

        elif choice == '3':
            john_harris_library.view_inventory()

        elif choice == '4':
            john_harris_library.display_books()
            book_index = int(input("Enter the index of the book you want to borrow: "))
            john_harris_library.borrow_book(book_index)

        elif choice == '0':
            print("Exiting...")
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
