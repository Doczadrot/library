from django.db import models

class Autor(models.Model):
    """
    Модель для представления автора книги
    """
    first_name = models.CharField(max_length=150, verbose_name='Имя')
    last_name = models.CharField(max_length=150, verbose_name='Фамилия')
    birth_date = models.DateField(verbose_name='Дата рождения')

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

    class Meta:
        verbose_name = 'Автор'
        verbose_name_plural = 'Авторы'


class Book(models.Model):
    """
    Модель для представления книги в библиотеке
    """
    title = models.CharField(max_length=200, verbose_name='Название')
    publication_date = models.DateField(verbose_name='Дата публикации')
    autor = models.ForeignKey(Autor, on_delete=models.CASCADE, verbose_name='books')
    #мы в книги укажем ревью
    review = models.TextField(null=True, blank=True)
    recommend = models.BooleanField(null=True, blank=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Книга'
        verbose_name_plural = 'Книги'
        ordering = ['title']
#Добавляем кастомные правадоступа
        permissions = [
            ('can_review_book', 'Просмотр книги'),
            ('can_recommend_book', 'Рекомендация книги')
        ]