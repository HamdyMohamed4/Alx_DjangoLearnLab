from django.contrib import admin

from .models import Book

admin.site.register(Book)

class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'publication_year')
    list_filter = ('author', 'publication_year')
    search_fields = ('title', 'author')

# Register the Book model with the custom admin class
admin.site.register(Book, BookAdmin)
