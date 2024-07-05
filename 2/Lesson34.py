#5. Создать класс Library, который будет управлять книгами. Каждая книга должна иметь атрибуты title, author и year.
#Класс Library должен иметь методы для добавления книги .add_book(), удаления книги .remove_book() и поиска книги по названию .find_book()

class AllBook:
    def __init__(self, title_pm: int, author_pm: str, year_pm: int):
        self.title = title_pm
        self.author = author_pm
        self.year = year_pm


class Library:
    def __init__(self):
        self.library = []

    def add_book(self, new_book: AllBook):
        self.library.append(new_book)
        return self.library
    def remove_book(self, remove: ):

book1 = AllBook(title_pm=1392, author_pm="Arthur Conan Doyle", year_pm=1887)
book2 = AllBook(title_pm=3636, author_pm="J. K. Rowling", year_pm=1997)

library = Library()
print(library.add_book(book1))
