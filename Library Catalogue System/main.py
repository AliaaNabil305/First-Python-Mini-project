class Book:
    def __init__(self, title, author, availability=True):
        self.title = title
        self.author = author
        self.availability = availability
    
    def display_book_info(self):
        """Displays the book's title, author, and availability status."""
        status = "Available" if self.availability else "Checked out"
        print(f"Title: {self.title}")
        print(f"Author: {self.author}")
        print(f"Availability: {status}")
    
    def check_out(self):
        """Checks out the book if it is available."""
        if self.availability:
            self.availability = False
            print(f"'{self.title}' has been checked out.")
        else:
            print(f"'{self.title}' is already checked out.")
    
    def return_book(self):
        """Returns the book if it was checked out."""
        if not self.availability:
            self.availability = True
            print(f"'{self.title}' has been returned.")
        else:
            print(f"'{self.title}' was not checked out.")

class LibraryCatalog:
    def __init__(self):
        self.books = []
    
    def add_book(self, book):
        """Adds a new book to the catalog."""
        self.books.append(book)
    
    def display_all_books(self):
        """Displays information about all books in the catalog."""
        for book in self.books:
            book.display_book_info()
            print()

catalog = LibraryCatalog()

book1 = Book("The Great Gatsby", "F. Scott Fitzgerald")
catalog.add_book(book1)

book2 = Book("1984", "George Orwell", False) 
catalog.add_book(book2)

print("Library Catalog:")
catalog.display_all_books()

book1.check_out() 
book2.check_out()  


book1.return_book() 
book2.return_book() 

print("Updated Library Catalog:")
catalog.display_all_books()
