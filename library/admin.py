from django.contrib import admin
from .models import Autor, Book # Убедитесь, что Autor и Book импортированы правильно

@admin.register(Autor)
class AutorAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'birth_date')
    search_fields = ('first_name', 'last_name')

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'publication_date', 'autor') # <-- ИЗМЕНЕНО!
    list_filter = ('publication_date', 'autor')          # <-- ИЗМЕНЕНО!
    search_fields = ('title', 'autor__first_name', 'autor__last_name')