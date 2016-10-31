from django.test import TestCase 
from django.core.urlresolvers import reverse
from app.models import Category, Book

class TestAppViews(TestCase):
    """ Tests the views display as expected """
    def setUp(self):
        self.test_category_data = {
            'name':'Initial Category'
        }
        

    def test_page_displays_content(self):
        url = reverse('homepage')
        resp = self.client.get(url)
        self.assertContains(resp, 'All Books')

    def test_page_to_add_books_renders(self):
        url = reverse('add_book')
        resp = self.client.get(url)
        self.assertContains(resp, 'New Book')

    def test_page_to_add_categories_renders(self):
        url = reverse('add_category')
        resp = self.client.get(url)
        self.assertContains(resp, 'New Category')

    def test_adding_category_from_the_frontend_works(self):
        url = reverse('add_category')
        categories_before = Category.objects.count()
        resp = self.client.post(url, self.test_category_data)
        categories_after = Category.objects.count()
        self.assertEqual(resp.status_code, 200)
        self.assertEqual(categories_after, categories_before + 1)

    def test_adding_book_from_the_frontend_works(self):
        url = reverse('add_book')
        before_addition = Book.objects.count()
        test_category = Category.objects.create(name='Test Category')
        test_book_data = {
            'title': 'Initial test title',
            'description': 'Book description',
            'category': test_category.id
        }
        resp = self.client.post(url, test_book_data)
        after_addition = Book.objects.count()
        self.assertEqual(after_addition, before_addition + 1)