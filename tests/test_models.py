from django.test import TestCase
from django.db.utils import IntegrityError
from faker import Factory
from api.models import Category, Book

fake = Factory.create()

class TestAppModels(TestCase):
    """docstring for TestAppModels"""

    def setUp(self):
        """ Set up data to be used within the class"""
        self.book_title = "Book title"
        self.description = fake.text()
        self.category_name = "Test category"
        self.initial_category = Category.objects.create(name=self.category_name)

    def tearDown(self):
        pass
    
    def test_models_save_new_data(self):
        before_addition = Book.objects.count()
        new_book = Book.objects.create(
            title=self.book_title, description=self.description, category=self.initial_category)
        after_addition = Book.objects.count()
        self.assertEqual(after_addition, before_addition + 1)
        
    def test_category_name_unique(self):
        new_category = Category.objects.create(name=self.category_name)
        self.assertRaises(IntegrityError)