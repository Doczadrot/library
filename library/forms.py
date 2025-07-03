from django import forms
from .models import Autor, Book

class AutorForm(forms.ModelForm):
    class Meta:
        model = Autor
        fields = ['first_name', 'last_name', 'birth_date']

class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'publication_date', 'autor']

