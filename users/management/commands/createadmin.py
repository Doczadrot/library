from django.core.management.base import BaseCommand # Импортируем базовый класс для создания команд
from django.contrib.auth import get_user_model     # Импортируем функцию для получения текущей модели пользователя

class Command(BaseCommand):
    # 'help' будет отображаться, когда пользователь выполнит 'python manage.py help createadmin'
    help = 'Создает суперпользователя с предопределенными данными (email: testadmin@admin.ru, пароль: 1234)'

    # Главный метод, который выполняется при вызове команды
    def handle(self, *args, **options):
        User = get_user_model() # Получаем текущую модель пользователя Django

        # Проверяем, существует ли пользователь с таким email, чтобы избежать дубликатов
        if User.objects.filter(email='testadmin@admin.ru').exists():
            self.stdout.write(self.style.WARNING('Пользователь testadmin@admin.ru уже существует. Создание пропущено.'))
            return # Выходим из функции, если пользователь уже есть

        # Создаем нового пользователя с указанными данными
        user = User.objects.create(
            email='testadmin@admin.ru',
            first_name='Admin',
            last_name='Admin',
        )

        # Хэшируем и устанавливаем пароль для пользователя
        user.set_password('1234')
        user.is_staff = True      # Даем пользователю доступ к админ-панели
        user.is_superuser = True  # Делаем пользователя суперпользователем (полные права)
        user.save()               # Сохраняем все изменения пользователя в базе данных (ОЧЕНЬ ВАЖНО!)

        # Выводим сообщение об успешном создании в консоль
        self.stdout.write(self.style.SUCCESS(f'Суперпользователь с email {user.email} успешно создан!'))