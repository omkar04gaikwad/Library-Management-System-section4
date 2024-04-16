import json

class Book:
    """
    Represents a book in the library.

    Attributes:
        title (str): The title of the book.
        author (str): The author of the book.
        isbn (str): The ISBN of the book.
        year (int): The year of publication of the book.
        copies (int): The number of copies available in the library.
    """

    def __init__(self, title, author, isbn, year, copies):
        """
        Initializes a Book object.

        Args:
            title (str): The title of the book.
            author (str): The author of the book.
            isbn (str): The ISBN of the book.
            year (int): The year of publication of the book.
            copies (int): The number of copies available in the library.
        """
        self.title = title
        self.author = author
        self.isbn = isbn
        self.year = year
        self.copies = copies
        
        self.book_info = {"title": self.title, "author": self.author, "isbn": self.isbn, "year": self.year, "copies": self.copies}
        
  

class Library:
    """
    Represents a library with a collection of books.

    Attributes:
        book_collection (list): A list containing Book objects representing the library's collection.
    """

    def __init__(self):
        """
        Initializes a Library object with an empty collection of books.
        """
        self.book_collection = []

    def add_book(self, title, author, isbn, year, copies):
        """
        Adds a new book to the library's collection.

        Args:
            title (str): The title of the book.
            author (str): The author of the book.
            isbn (str): The ISBN of the book.
            year (int): The year of publication of the book.
            copies (int): The number of copies available in the library.
        """
        pass

    def display_all_books(self):
        """
        Displays all books in the library's collection.
        """
        pass

    def search_by_title(self, title):
        """
        Searches for books by title and displays matching books.

        Args:
            title (str): The title to search for.
        """
        pass

    def remove_book(self, isbn):
        """
        Removes a book from the library's collection by ISBN.

        Args:
            isbn (str): The ISBN of the book to remove.
        """
        pass

    def update_book(self, isbn, new_info):
        """
        Updates information of a book in the library's collection by ISBN.

        Args:
            isbn (str): The ISBN of the book to update.
            new_info (dict): A dictionary containing the updated information.
        """
        pass

    def count_books(self):
        """
        Counts the total number of books in the library's collection.

        Returns:
            int: The total number of books.
        """
        pass

    def list_books_by_author(self, author):
        """
        Lists all books by a specific author.

        Args:
            author (str): The author's name.
        """
        pass

    def check_out_book(self, isbn):
        """
        Checks out a book from the library's collection by ISBN.

        Args:
            isbn (str): The ISBN of the book to check out.
        """
        pass

    def return_book(self, isbn):
        """
        Returns a checked-out book to the library's collection by ISBN.

        Args:
            isbn (str): The ISBN of the book to return.
        """
        for book in book_collection:
            if book.isbn == isbn:
                book.copies += 1
        pass

    def search_by_author(self, author):
        """
        Searches for books by author and displays matching books.

        Args:
            author (str): The author's name.
        """
        for book in book_collection:
            if book.author == author:
                print("Name:", book.name, "Author:", book.author)
        pass

    def search_by_year(self, year):
        """
        Searches for books by publication year and displays matching books.

        Args:
            year (int): The publication year.
        """
        pass

    def list_all_authors(self):
        """
        Lists all unique authors in the library's collection.
        """
        pass

    def save_collection_to_file(self, filename):
        """
        Saves the current state of the library's collection to a file in JSON format.

        Args:
            filename (str): The name of the file to save.
        """
        pass

    def load_collection_from_file(self, filename):
        """
        Loads the library's collection from a file in JSON format.

        Args:
            filename (str): The name of the file to load.
        """
        pass

    def sort_books_by_title(self):
        """
        Sorts the library's collection of books by title and displays them.
        """
        pass

    def unique_isbn_check(self, isbn):
        """
        Checks if a given ISBN is unique in the library's collection.

        Args:
            isbn (str): The ISBN to check.

        Returns:
            bool: True if the ISBN is unique, False otherwise.
        """
        pass

    def book_recommendation(self, author=None, year=None):
        """
        Provides a recommendation for a book based on the given author or publication year.

        Args:
            author (str): The author's name for recommendation.
            year (int): The publication year for recommendation.
        """
        pass

    def total_copies_count(self):
        """
        Calculates the total number of book copies in the library's collection.

        Returns:
            int: The total number of book copies.
        """
        pass

    def most_published_author(self):
        """
        Determines which author has the most books in the library's collection and displays the result.
        """
        pass

    def filter_books_by_year_range(self, start_year, end_year):
        """
        Filters and displays books published within a specific year range.

        Args:
            start_year (int): The start year of the range.
            end_year (int): The end year of the range.
        """
        pass

    def longest_book_title(self):
        """
        Finds the book with the longest title in the library's collection and displays it.
        """
        pass

    def backup_collection(self, backup_filename):
        """
        Creates a backup of the library's collection to a separate file.

        Args:
            backup_filename (str): The name of the backup file.
        """
        pass

if __name__ == "__main__":
    print("**********LIBRARY MANAGEMENT***********")
    """
    library = Library()
    library.add_book("Harry Potter", "J.K. Rowling", "1234567890", 1997, 3)
    library.add_book("Python Programming", "Test Test", "999888777", 2020, 5)
    library.display_all_books()
    library.search_by_title("Harry Potter")
    library.remove_book("1234567890")
    library.update_book("0987654321", {'copies': 7})
    print("Total books:", library.count_books())
    library.list_books_by_author("J.K. Rowling")
    library.check_out_book("0987654321")
    library.return_book("0987654321")
    library.search_by_author("Test")
    library.search_by_year(2020)
    library.list_all_authors()
    library.save_collection_to_file("library.json")
    library.load_collection_from_file("library.json")
    library.sort_books_by_title()
    print("Is ISBN unique:", library.unique_isbn_check("1234567890"))
    library.book_recommendation(author="J.K. Rowling")
    print("Total copies:", library.total_copies_count())
    library.most_published_author()
    library.filter_books_by_year_range(1990, 2000)
    library.longest_book_title()
    library.backup_collection("library_backup.json")
    """
