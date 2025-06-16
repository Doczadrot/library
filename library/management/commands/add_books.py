from django.core.management.base import BaseCommand
from library.models import Autor, Book

class Command(BaseCommand):
    """Команда Django для добавления книг в базу данных."""
    help = 'Добавляет книги в базу данных'

    def handle(self, *args, **kwargs):
        """Основной метод команды, выполняющий добавление книг."""
        # Создаем авторов
        author = Autor.objects.create(first_name='John', last_name='Doe', birth_date='1990-01-01')

        books = [
            Book(title='Вишневый сад', publication_date='1904-01-01', autor=author),
            Book(title='Три сестры', publication_date='2022-02-01', autor=author),
            Book(title='Война и мир', publication_date='1869-01-01', autor=author),
        ]

        for book in books:
            book.save()
            self.stdout.write(self.style.SUCCESS(f'Successfully added book: {book.title}'))