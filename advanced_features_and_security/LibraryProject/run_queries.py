import os
import django

# Set up Django environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'LibraryProject.settings')
django.setup()

from relationship_app.query_samples import get_books_by_author, list_books_in_library, get_librarian_for_library

# Example usage
books_by_author = get_books_by_author('Author Name')
for book in books_by_author:
    print(book.title)

books_in_library = list_books_in_library('Library Name')
for book in books_in_library:
    print(book.title)

librarian = get_librarian_for_library('Library Name')
print(librarian.name)
