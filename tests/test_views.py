from django.test import TestCase 
from django.core.urlresolvers import reverse
from app.models import Category, Book

class TestAppViews(TestCase):
    """ Tests the views display as expected """
    def setUp(self):
        self.test_category_data = {
            'name':'Initial Category'
        }
        self.test_category = Category.objects.create(name='Test Category')
        self.test_book_item = Book.objects.create(
            title='Book Title', description='Book description', 
            category=self.test_category)
        self.test_book_data = {
            'title': 'Initial test title',
            'description': 'Book description',
            'category': self.test_category.id
        }
        self.add_book_url = reverse('add_book')
        self.add_category_url = reverse('add_category')
        self.homepage_url = reverse('homepage')
        self.book_detail_url = reverse('book_detail', kwargs={'id': self.test_book_item.id})
        

    def test_page_displays_content(self):
        resp = self.client.get(self.homepage_url)
        self.assertContains(resp, 'All Books')

    def test_page_to_add_books_renders(self):
        resp = self.client.get(self.add_book_url)
        self.assertContains(resp, 'New Book')

    def test_page_to_add_categories_renders(self):
        resp = self.client.get(self.add_category_url)
        self.assertContains(resp, 'New Category')

    def test_adding_category_from_the_frontend_works(self):
        categories_before = Category.objects.count()
        resp = self.client.post(self.add_category_url, self.test_category_data)
        categories_after = Category.objects.count()
        self.assertEqual(resp.status_code, 200)
        self.assertEqual(categories_after, categories_before + 1)

    def test_adding_book_from_the_frontend_works(self):
        before_addition = Book.objects.count()
        resp = self.client.post(self.add_book_url, self.test_book_data)
        after_addition = Book.objects.count()
        self.assertEqual(after_addition, before_addition + 1)

    def test_added_book_can_be_viewed_from_the_front_end(self):
        new_book = self.client.post(self.add_book_url, self.test_book_data)
        resp = self.client.get(self.homepage_url)
        self.assertContains(resp, self.test_book_data['title'])

    def test_user_can_view_each_book(self):
        new_book = self.client.post(self.add_book_url, self.test_book_data)
        resp = self.client.get(self.book_detail_url)
        self.assertContains(resp, self.test_book_item.title)