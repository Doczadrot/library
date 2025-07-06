from django.urls import path
from django.contrib import admin
from .views import books_list, books_detail

app_name = "library"

urlpatterns = [
    path('books_list/', books_list, name='books_list'),
    path('books_detail/<int:book_id>/', books_detail, name='books_detail'),
]
