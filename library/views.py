
from django.http import HttpResponse, HttpResponseForbidden
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy
from .forms import AutorForm, BookForm
from .models import Book, Autor
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView, View
from django.views.decorators.cache import cache_page # импортирием для работы с кэшем страницы
from django.utils.decorators import method_decorator   # для указания конкретного кэша
from django.core.cache import cache

from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin

class AutorListView(ListView):
    model = Autor
    template_name = 'library/autors_list.html'
    context_object_name = 'autors'
    #переопределяем кверисет
    def get_queryset(self):
        queryset = cache.get('autors_queryset')

#если кверисет пустой
        if not queryset:
            queryset = super().get_queryset() # мы выводим  значения значеги кверисет из БД делаем через супер

            cache.set('autors_queryset', queryset, 60 * 15)
        return queryset

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


@method_decorator(cache_page(60 * 15), name='dispatch')
class BooksListView(LoginRequiredMixin, PermissionRequiredMixin, ListView):
    model = Book
    template_name = 'library/books_list.html'
    context_object_name = 'books'
    permission_required = 'library.veiw_book'



class BookCreateView(LoginRequiredMixin, PermissionRequiredMixin ,CreateView):
    model = Book
    form_class = BookForm
    template_name = 'library/book_form.html'
    success_url = reverse_lazy('library:books_list')
    permission_required = 'library.add_book'


@method_decorator(cache_page(60 * 15), name='dispatch')
class BookDetailView(LoginRequiredMixin,  DetailView):
    model = Book
    template_name = 'library/book_detail.html'
    context_object_name = 'book'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['autor_books_count'] = Book.objects.filter(autor=self.object.autor).count()
        return context

class BookUpdateView(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    model = Book
    form_class = BookForm
    template_name = 'library/book_form.html'
    success_url = reverse_lazy('library:books_list')
    permission_required = 'library.change_book'

class BookDeleteView(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    model = Book
    success_url = reverse_lazy('library:books_list')
    template_name = 'library/book_confirm_delete.html'
    permission_required = 'library.delete_book'

# Cоздаем предоставление
class ReviewBookView(LoginRequiredMixin, View):
    def post(self, request, book_id):
        book = get_object_or_404(Book, id=book_id)

        if not request.user.has_perm('library.can_review_book'):
            return HttpResponseForbidden('У вас нет прав для рецензирования')

        book.review = request.POST.get('review')
        book.save()

        return redirect('library:book_detail', pk=book_id)

class RecommendBookView(LoginRequiredMixin, View):
    def post(self, request, book_id):
        book = get_object_or_404(Book, id=book_id)

        if not request.user.has_perm('library.can_recommend_book'):
            return HttpResponseForbidden('У вас нет прав для рекомендации книги')

        book.recommend = True
        book.save()

        return redirect('library:book_detail', pk=book_id)