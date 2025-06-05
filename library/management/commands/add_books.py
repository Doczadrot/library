from django.core.management.base import BaseCommand
from library.models import Autor, Book

class Command(BaseCommand):
    help = 'Add books to the database'

    def handle(self, *args, **kwargs):
        # Создаем авторов
        author = Autor.objects.create(first_name='John', last_name='Doe', birth_date='1990-01-01')


    books = [
        Book(title='Вишневый сад', publication_date='1904-01-01', autor=autor),
        Book(title='Три сестры', publication_date='2022-02-01', autor=None),
        Book(title='Book 3', publication_date='2022-03-01', autor=autor),
    ]


    for book in books:
        book, created = Book.objects.get_or_create(
            title=book.title,
            publication_date=book.publication_date,
            autor=book.autor
        )
        if created:
            self.stdout.write(self.style.SUCCESS(f'Successfully added book: {book.title}'))