from django.urls import path
from django.contrib import admin

from .views import RecommendBookView, ReviewBookView, BooksListView, BookDetailView, BookCreateView, BookDeleteView, BookUpdateView, AutorCreateView, AutorUpdateView, AutorListView

app_name = "library"

urlpatterns = [
    path('autors/', AutorListView.as_view(), name='autors_list'),
    path('autor/new/',AutorCreateView.as_view(), name = 'autors_create'),
    path('autor/update/<int:pk>/',AutorUpdateView.as_view(), name = 'autor_update'),
    path('books/', BooksListView.as_view(), name='books_list'),
    path('books/<int:pk>/', BookDetailView.as_view(), name='book_detail'),
    path('books/new/', BookCreateView.as_view(), name='book_create'),
    path('books/<int:pk>/update/', BookUpdateView.as_view(), name='book_update'),
    path('books/<int:pk>/delete/', BookDeleteView.as_view(), name='book_delete'),
    path('books/recommend/<int:book_id>/', RecommendBookView.as_view(), name='book_recommend'),
    path('books/review/<int:book_id>/', ReviewBookView.as_view(), name='book_review'),
]