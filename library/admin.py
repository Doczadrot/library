<<<<<<< HEAD

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
=======
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
>>>>>>> f5d968f8038b6d5b45880bb7b002566048915f4a
