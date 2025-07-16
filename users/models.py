# users/models.py
from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    """
    Пользовательская модель пользователя, расширяющая AbstractUser Django.
    Использует email в качестве основного уникального идентификатора для входа.
    """
    email = models.EmailField(unique=True, verbose_name='Email адрес') # Создаем поле для ввода email (уникальность включена)
    phone_number = models.CharField(max_length=15, blank=True, null=True, verbose_name='Номер телефона') # Для хранения номера (длиной 15 и может быть пустым)
    avatar = models.ImageField(upload_to='avatars/', blank=True, null=True, verbose_name='Аватар') # Для изображения (адрес хранения и может быть пустым)
    username = models.CharField(max_length=150, unique=False, blank=True, null=True)

    USERNAME_FIELD = 'email'  # Указываем, что для входа будет использоваться email
    REQUIRED_FIELDS = [] # 'username' остается обязательным полем для заполнения при создании пользователя через manage.py createsuperuser, даже если логин по email

    def __str__(self):
        return self.email

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'