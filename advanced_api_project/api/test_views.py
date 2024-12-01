from rest_framework.test import APITestCase, APIClient
from rest_framework import status
from django.contrib.auth.models import User
from .models import Author, Book

class BookAPITests(APITestCase):
    def setUp(self):
        # Create test users
        self.user = User.objects.create_user(username='testuser', password='password123')
        
        # Create test data
        self.author = Author.objects.create(name="John Doe")
        self.book1 = Book.objects.create(title="Book One", publication_year=2021, author=self.author)
        self.book2 = Book.objects.create(title="Book Two", publication_year=2022, author=self.author)

        # Authenticate client
        self.client = APIClient()
        self.client.login(username='testuser', password='password123')

    def test_list_books(self):
        """
        Test retrieving the list of books.
        """
        response = self.client.get('/api/books/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)
        self.assertIn('Book One', [book['title'] for book in response.data])

    def test_create_book(self):
        """
        Test creating a new book.
        """
        data = {
            "title": "New Book",
            "publication_year": 2023,
            "author": self.author.id
        }
        response = self.client.post('/api/books/', data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Book.objects.count(), 3)
        self.assertEqual(Book.objects.last().title, "New Book")

    def test_update_book(self):
        """
        Test updating an existing book.
        """
        data = {
            "title": "Updated Book One",
            "publication_year": 2021,
            "author": self.author.id
        }
        response = self.client.put(f'/api/books/{self.book1.id}/', data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.book1.refresh_from_db()
        self.assertEqual(self.book1.title, "Updated Book One")

    def test_delete_book(self):
        """
        Test deleting a book.
        """
        response = self.client.delete(f'/api/books/{self.book1.id}/')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Book.objects.count(), 1)

    def test_filter_books(self):
        """
        Test filtering books by publication year.
        """
        response = self.client.get('/api/books/?publication_year=2022')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['title'], "Book Two")

    def test_search_books(self):
        """
        Test searching books by title.
        """
        response = self.client.get('/api/books/?search=Book')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)

    def test_order_books(self):
        """
        Test ordering books by publication year.
        """
        response = self.client.get('/api/books/?ordering=publication_year')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data[0]['title'], "Book One")
