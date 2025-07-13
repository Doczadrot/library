from django import template
from django.http import HttpResponse
from django.shortcuts import render
from django.urls import reverse_lazy
from .forms import AutorForm, BookForm

from .models import Book, Autor

from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from django.contrib.auth.mixins import LoginRequiredMixin

class AutorListView(ListView):
    model = Autor
    template_name = 'library/autors_list.html'
    context_object_name = 'autors'


class AutorCreateView(LoginRequiredMixin, CreateView):
    model = Autor
    form_class = AutorForm
    template_name = 'library/autor_form.html'
    success_url = reverse_lazy('library:autors_list')

class AutorUpdateView(LoginRequiredMixin, UpdateView):
    model = Autor
    form_class = AutorForm
    template_name = 'library/autor_form.html'
    success_url = reverse_lazy('library:autors_list')



class BooksListView(ListView):
    model = Book
    template_name = 'library/books_list.html'
    context_object_name = 'books'



class BookCreateView(LoginRequiredMixin ,CreateView):
    model = Book
    form_class = BookForm
    template_name = 'library/book_form.html'
    success_url = reverse_lazy('library:books_list')

class BookDetailView(DetailView):
    model = Book
    template_name = 'library/book_detail.html'
    context_object_name = 'book'


class BookUpdateView(LoginRequiredMixin ,UpdateView):
    model = Book
    form_class = BookForm
    template_name = 'library/book_form.html'
    success_url = reverse_lazy('library:books_list')

class BookDeleteView(LoginRequiredMixin, DeleteView):
    model = Book
    success_url = reverse_lazy('library:books_list')
    template_name = 'library/book_confirm_delete.html'

