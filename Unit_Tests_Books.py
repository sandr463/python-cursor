import unittest
from unittest import TestCase
import Book_Classes as bc

book = None

class Book_Unit_Test(TestCase):
    @classmethod
    def setUpClass(cls):
        print('setUpClass in Book')

    @classmethod
    def tearDownClass(cls):
        print('tearDownClass is Book')

    def setUp(self):
        self.name = 'Book_name'
        self.author = 'Book_author'

    def tearDown(self):
        print('tearDown: Clean\n')

    def book_test_creation(self):
        class_instace = bc.Book(self.name, self.author)
        self.assertIsNotNone(class_instace)
        self.assertEqual(class_instace.name, self.name)
        self.assertEqual(class_instace.author, self.author)

    def book_str_test(self):
        class_instance = bc.Book(self.name, self.author)
        self.assertEqual(f'{class_instance.name} is {class_instance.author}', f'{self.name} is {self.author}')


class BookShelf_Unit_Test(TestCase):
    @classmethod
    def setUpClass(cls):
        print('setUpClass in BoolShelf')

    @classmethod
    def tearDownClass(cls):
        print('tearDownClass is BookShelf')

    def setUp(self):
        self.shelf_name = 'Book_shelf_1'
        self.book_1 = bc.Book('Book_1', 'Author_1')
        self.book_2 = bc.Book('Book_2', 'Author_2')

        self.shelf = bc.BookShelf('shelf_1')

    def tearDown(self):
        print('tearDown: CLean\n')

    def book_shelf_test_creation(self):
        class_instance = bc.BookShelf(self.shelf_name)
        self.assertIsNotNone(class_instance)
        self.assertEqual(class_instance.shelf_name, self.shelf_name)

    def book_shelf_add_test(self):
        self.shelf.__add__(self.book_1)
        self.shelf.__add__(self.book_2)
        self.assertIn(self.book_1, self.shelf.books)
        self.assertIn(self.book_2, self.shelf.books)

    def book_shelf_description_test(self):
        coma = ', '
        self.assertEqual(self.shelf.description, f'BookShelf consists of {coma.join(book.name for book in self.shelf.books)}')


if __name__ == '__main__':
    unittest.main()
