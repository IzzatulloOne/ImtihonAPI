from django.urls import path
from .views import BookListCreateView, BookDetailView, AuthorListCreateView, AuthorDetailView, GenreListCreateView, GenreDetailView, PublishmentListCreateView, PublishmentRetrieveUpdateDestroyView

urlpatterns = [
    path('books/', BookListCreateView.as_view(), name='book-list-create'),
    path('books/<int:pk>/', BookDetailView.as_view(), name='book-detail'),
    path('authors/', AuthorListCreateView.as_view(), name='author-list-create'),
    path('authors/<int:pk>/', AuthorDetailView.as_view(), name='author-detail'),
    path('genres/', GenreListCreateView.as_view(), name='genre-list-create'),
    path('genres/<int:pk>/', GenreDetailView.as_view(), name='genre-detail'),
    path('publishments/', PublishmentListCreateView.as_view(), name='publishment-list-create'),
    path('publishments/<int:pk>/', PublishmentRetrieveUpdateDestroyView.as_view(), name='publishment-detail'),
]