from django import template
from django.http import HttpResponse
from django.shortcuts import render
from .models import Book

#Эта функция предназначена для показа списка всех книг.
def books_list(request):
    """Отображает список книг."""
    books = Book.objects.all() #говорим джанго - выведи все обьекты относящиеся  к классу Book в переменную books
    #создаем словарь, где ключ 'books' и значение books
    context = {'books': books}
    return render(request, 'library/books_list.html', context)


#второ контролеер - детальное изображение книги
def books_detail(request, book_id):
    """Отображает детали книги."""
    book = Book.objects.get(id=book_id)
    context = {'book': book}
    return render(request, template_name='library/books_detail.html', context=context)


