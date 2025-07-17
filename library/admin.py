
from django.contrib import admin
from .models import Autor, Book


@admin.register(Autor) # Регистрируем Autor
class AutorAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'birth_date')
    search_fields = ('first_name', 'last_name')



@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    # Используйте правильные имена полей, как определено в models.py
    # publication_date - это ваше поле с датой публикации в models.py
    list_display = ('title', 'autor', 'publication_date')
    list_filter = ('publication_date', 'autor')
    search_fields = ('title', 'autor__first_name', 'autor__last_name',)

