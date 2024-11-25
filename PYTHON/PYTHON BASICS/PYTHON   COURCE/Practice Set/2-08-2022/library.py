#Build a class Library with a list of books. Implement methods to add a book, display all books, and search for a book by title.

class Library:
    def __init__(self):
        self.book_list = []

    def add_book(self,book_name):
        self.book_list.append(book_name)

    def display_books(self):
        for i in self.book_list:
            print(i,end=" ")

    def search(self,title):
        for i in self.book_list:
            if i == title:
                print("Available")
            else:
                print("Not available")

lab1 = Library()
lab1.add_book("Hands on machine learning")
lab1.display_books()
        