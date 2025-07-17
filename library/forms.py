from django import forms
from .models import Autor, Book
from django.core.exceptions import ValidationError

class AutorForm(forms.ModelForm):
    class Meta:
        model = Autor
        fields = ['first_name', 'last_name', 'birth_date']

    def __init__(self, *args, **kwargs):
        super(AutorForm, self).__init__(*args, **kwargs)
        self.fields['first_name'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Введите имя'})
        self.fields['last_name'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Введите Фамилию'})
        self.fields['birth_date'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Введите дату рождения'})
    def clean(self):
        #clean =  метод для выполнения валиадации для нескольких полей
        cleaned_data = super().clean()
        first_name = cleaned_data.get('first_name')
        last_name = cleaned_data.get('last_name')

        if Autor.objects.filter(first_name=first_name, last_name=last_name).exists():
            raise ValidationError('Автор с таким именем и фамилией уже существует.')

        return cleaned_data


class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'publication_date', 'autor']

    def __init__(self, *args, **kwargs):
        super(BookForm, self).__init__(*args, **kwargs)
        self.fields['title'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Введите Названия книги'})
        self.fields['publication_date'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Введите дату публикации'})
        self.fields['autor'].widget.attrs.update({'class': 'form-control'})