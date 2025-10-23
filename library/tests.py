from django.contrib.auth.models import User
from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient
from .models import Author, Book

class BookModelTest(TestCase):
    def setUp(self):
        self.author = Author.objects.create(first_name="Лев", last_name="Толстой")
        self.book_data = {
            'title': 'Война и мир',
            'author': self.author,
            'publication_year': 1869,
            'genre': 'Роман',
            'category': 'fiction',
            'publisher': 'АСТ'
        }

    def test_unique_constraint(self):
        Book.objects.create(**self.book_data)
        with self.assertRaises(Exception):
            Book.objects.create(**self.book_data)

class BookAPITest(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.author = Author.objects.create(first_name="Фёдор", last_name="Достоевский")
        self.admin_user = User.objects.create_superuser(
            username='admin', password='adminpass'
        )
        self.book = Book.objects.create(
            title='Преступление и наказание',
            author=self.author,
            publication_year=1866,
            genre='Роман',
            category='fiction',
            publisher='Эксмо'
        )

    def test_create_book_as_admin(self):
        self.client.force_authenticate(user=self.admin_user)
        url = reverse('library:book-create')
        data = {
            'title': 'Идиот',
            'author_id': self.author.id,
            'publication_year': 1869,
            'genre': 'Роман',
            'category': 'fiction',
            'publisher': 'Азбука'
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_create_book_as_anonymous(self):
        url = reverse('library:book-create')
        data = {
            'title': 'Бесы',
            'author_id': self.author.id,
            'publication_year': 1872,
            'genre': 'Роман',
            'category': 'fiction',
            'publisher': 'Просвещение'
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_search_books(self):
        url = reverse('library:book-search')
        response = self.client.get(url, {'q': 'Преступление'})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertIn('Преступление', response.data[0]['title'])