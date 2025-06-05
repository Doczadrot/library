
from django.contrib import admin
from .models import Autor, Book  # Импортируем наши модели

@admin.register(Book) # Декоратор для регистрации модели Автор в административной панели
class BookAdmin(admin.ModelAdmin):
    """
    Настройки отображения модели Книга в административной панели
    """
    list_display = ('title', 'autor', 'publication_date') # Поля для отображения в списке записей
# admin.site.register(Autor) # Регистрируем модель Автор в админке для управления данными
# admin.site.register(Book) # Регистрируем модель Книга в админке для управления данными
# # Register your models here.
