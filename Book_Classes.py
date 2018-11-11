class Book():
    name = None
    author = None

    def __init__(self, name, author):
        self.name = name
        self.author = author

    def __str__(self):
        return f'{self.name} is {self.author}'

book = Book('Test', 'Tester')
book1 = Book('Test1', 'Tester')
book2 = Book('Test2', 'Tester')
print(book)


class BookShelf():
    def __init__(self, shelf_name):
        self.shelf_name = shelf_name
        self.books = []

    def __add__(self, book):
        return self.books.append(book)

    @property
    def description(self):
        coma = ', '
        return f'BookShelf consists of {coma.join(book.name for book in self.books)}'

book_shelf = BookShelf('shelf')

book_shelf.__add__(book)
book_shelf.__add__(book1)
book_shelf.__add__(book2)

print(book_shelf.description)




