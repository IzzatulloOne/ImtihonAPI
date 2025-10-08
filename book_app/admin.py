from django.contrib import admin
from .models import Book, Author, Genre, Publishment

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'genre', 'publishment', 'published_date', 'isbn')
    search_fields = ('title', 'author__first_name', 'author__last_name', 'genre__name', 'publishment__name')
    list_filter = ('genre', 'author', 'publishment')
    ordering = ('title',)


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name')
    search_fields = ('first_name', 'last_name')
    ordering = ('last_name', 'first_name')


@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)
    ordering = ('name',)


@admin.register(Publishment)
class PublishmentAdmin(admin.ModelAdmin):
    list_display = ('name', 'address')
    search_fields = ('name', 'address')
    ordering = ('name',)
    