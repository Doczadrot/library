# C:\Users\ivan\Desktop\LybruryDjango\library\admin.py

from django.contrib import admin
from .models import Autor, Book # Импортируем обе модели ОДИН РАЗ, в начале файла

# --- Регистрация модели Autor ---
@admin.register(Autor) # Регистрируем Autor
class AutorAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'birth_date')
    search_fields = ('first_name', 'last_name')

# --- Регистрация модели Book ---
# Должен быть ТОЛЬКО ОДИН класс BookAdmin с @admin.register(Book)
@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    """
    Административная панель для управления книгами
    """
    # Используйте правильные имена полей, как определено в models.py
    # publication_date - это ваше поле с датой публикации в models.py
    list_display = ('title', 'autor', 'publication_date')
    list_filter = ('publication_date', 'autor')
    search_fields = ('title', 'autor__first_name', 'autor__last_name',)

