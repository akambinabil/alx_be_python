# library_management.py

class Book:
    """
    Represents a book in the library with a title, author, and availability status.
    """
    def __init__(self, title, author):
        """
        Initializes a new Book instance.

        Args:
            title (str): The title of the book.
            author (str): The author of the book.
        """
        self.title = title  # Public attribute
        self.author = author  # Public attribute
        self._is_checked_out = False  # Private attribute to track availability

    def check_out(self):
        """
        Marks the book as checked out (unavailable).
        Returns True if successful, False if already checked out.
        """
        if not self._is_checked_out:
            self._is_checked_out = True
            return True
        print(f"'{self.title}' is already checked out.")
        return False

    def return_book(self):
        """
        Marks the book as available (returned).
        Returns True if successful, False if not currently checked out.
        """
        if self._is_checked_out:
            self._is_checked_out = False
            return True
        print(f"'{self.title}' is not currently checked out.")
        return False

    def is_available(self):
        """
        Checks if the book is currently available.

        Returns:
            bool: True if available, False otherwise.
        """
        return not self._is_checked_out

    def __str__(self):
        """
        Returns a user-friendly string representation of the Book object.
        """
        return f"{self.title} by {self.author}"


class Library:
    """
    Manages a collection of Book instances, providing functionalities to add,
    check out, return, and list available books.
    """
    def __init__(self):
        """
        Initializes a new Library instance with an empty list of books.
        """
        self._books = []  # Private list to store Book objects

    def add_book(self, book):
        """
        Adds a Book object to the library's collection.

        Args:
            book (Book): The Book object to add.
        """
        if not isinstance(book, Book):
            print("Error: Only Book objects can be added to the library.")
            return

        # Optional: Prevent adding the same book multiple times (e.g., by title and author)
        # For simplicity, we'll allow duplicates for now unless specified otherwise.
        self._books.append(book)
        print(f"Added '{book.title}' to the library.")

    def _find_book(self, title):
        """
        Helper method to find a book by its title in the library's collection.
        Returns the Book object if found, otherwise None.
        """
        # Iterate through the private list of books to find a match
        for book in self._books:
            if book.title == title:
                return book
        return None # Book not found

    def check_out_book(self, title):
        """
        Attempts to check out a book by its title.

        Args:
            title (str): The title of the book to check out.
        """
        book_to_check_out = self._find_book(title)
        if book_to_check_out:
            if book_to_check_out.check_out(): # Delegate the actual check-out to the Book object
                print(f"Successfully checked out '{title}'.")
            # Message for already checked out handled by Book.check_out()
        else:
            print(f"'{title}' not found in the library.")

    def return_book(self, title):
        """
        Attempts to return a book by its title.

        Args:
            title (str): The title of the book to return.
        """
        book_to_return = self._find_book(title)
        if book_to_return:
            if book_to_return.return_book(): # Delegate the actual return to the Book object
                print(f"Successfully returned '{title}'.")
            # Message for not checked out handled by Book.return_book()
        else:
            print(f"'{title}' not found in the library.")

    def list_available_books(self):
        """
        Lists all books currently available in the library.
        """
        available_found = False
        for book in self._books:
            if book.is_available(): # Check availability using the Book's method
                print(book) # Uses the __str__ method of the Book object
                available_found = True
        if not available_found:
            print("No books currently available.")