from django import template
from django.http import HttpResponse
from django.shortcuts import render
from django.urls import reverse_lazy

from .models import Book
from django.views.generic import ListView, DeleteView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView


class BooksListView(ListView):
    model = Book
    template_name = 'library/books_list.html'
    context_object_name = 'books'

class BookCreateView(CreateView):
    model = Book
    fields = ['title', 'publication_date', 'autor']
    template_name = 'library/book_form.html'
    success_url = reverse_lazy('library:books_list')

class BookDetailView(DetailView):
    model = Book
    template_name = 'library/book_detail.html'
    context_object_name = 'book'


class BookUpdateView(UpdateView):
    model = Book
    fields = ['title', 'autor', 'publication_date']
    template_name = 'library/book_form.html'
    success_url = reverse_lazy('library:books_list')

class BookDeleteView(DeleteView):
    model = Book
    success_url = reverse_lazy('library:books_list')
    template_name = 'library/book_confirm_delete.html'

