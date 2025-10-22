from django.contrib import admin
from .models import Author, Book

@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name')
    search_fields = ('first_name', 'last_name')

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'publication_year', 'category', 'publisher')
    list_filter = ('category', 'genre', 'publication_year')
    search_fields = ('title', 'author__first_name', 'author__last_name', 'publisher')