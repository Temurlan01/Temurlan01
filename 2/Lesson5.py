class Book:
    def __init__(self,title_pm:str, author_pm:str):
        self.title = title_pm
        self.author = author_pm

    def display_info(self):
        print(f"название книги: {self.title},автор:{self.author}")

book1 = Book(title_pm="Гари Поттер", author_pm="J. K. Rowling")
book2 = Book(title_pm="Шерлок Хомс", author_pm="Arthur Conan Doyle")
book1.display_info()


class Library:
    def __init__(self):
        self.books = []

    def add_book(self, new_book: Book):
        self.books.append(new_book)
    def list_books(self):
        return self.books
    def remove_book(self, rem_book: Book):
        self.books.remove(rem_book)
    def find_book_by_title(self,book_title:str):
        for item in self.books:
            if item.title == book_title:
                return item
            else:
                print("Такой книги нет")
    def find_book_by_author(self, author_name):
        for answer in self.books:
            pass


lib = Library()

lib.add_book(book1)
print(lib.list_books())
lib.add_book(book2)
print(lib.list_books())
#lib.remove_book(book2)
#print(lib.list_books())
lib.find_book_by_title("Гари Поттер")


