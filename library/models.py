from django.db import models

# Модель для представления Автора книги
class Autor(models.Model):
    # Имя автора, текстовое поле с максимальной длиной 150 символов.
    # verbose_name - человекочитаемое имя поля, используется в админке Django.
    first_name = models.CharField(max_length=150, verbose_name='Имя')
    # Фамилия автора, аналогично имени.
    last_name = models.CharField(max_length=150, verbose_name='Фамилия')
    # Дата рождения автора, поле для хранения даты.
    birth_date = models.DateField(verbose_name='Дата рождения')

    # Метод __str__ определяет строковое представление объекта.
    # Используется, например, в админке Django для отображения объекта в списках.
    def __str__(self):
        return f"{self.first_name} {self.last_name}" # Возвращает полное имя автора
        
    # Класс Meta содержит метаданные модели.
    class Meta:
        verbose_name = 'Автор'  # Имя модели в единственном числе для админки
        verbose_name_plural = 'Авторы' # Имя модели во множественном числе для админки
        # ordering = ['last_name'] # Пример: сортировка авторов по фамилии по умолчанию

# Модель для представления Книги
class Book(models.Model):
    # Название книги, текстовое поле с максимальной длиной 200 символов.
    title = models.CharField(max_length=200, verbose_name='Название')
    # Дата публикации книги, поле для хранения даты.
    publication_date = models.DateField(verbose_name='Дата публикации')
    # Связь с моделью Autor (один автор может иметь много книг).
    # on_delete=models.CASCADE означает, что при удалении автора, все его книги также будут удалены.
    autor = models.ForeignKey(Autor, on_delete=models.CASCADE, verbose_name='Автор')

    # Строковое представление объекта Книги.
    def __str__(self):
        return self.title # Возвращает название книги

    # Метаданные для модели Книги.
    class Meta:
        verbose_name = 'Книга' # Имя модели в единственном числе
        verbose_name_plural = 'Книги' # Имя модели во множественном числе
        ordering = ['title'] # Книги по умолчанию будут отсортированы по названию
