#задание 1: «Книга»:
#Создайте класс Book с атрибутами для названия книги, для имени автора и количество страниц.
#Напишите метод, который выводит краткую информацию о книге.
#Создайте несколько объектов класса Book и выведите информацию о каждой книге.

class Book:

    def __init__(self, pages_pm, Author_pm, name_pm):
        self.pages = pages_pm
        self.Author = Author_pm
        self.name = name_pm

    def get_info(self):
        return f"Название книги: {self.name}, Число страниц: {self.pages}, Автор: {self.Author}"

math = Book(pages_pm=120, Author_pm="Моро, Бантова, Бельтюкова", name_pm="Математика")
english = Book(pages_pm=35, Author_pm="Назарбекова Г. Д.", name_pm="Английский")

print(math.get_info())