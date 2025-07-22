
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.utils import timezone

class CustomUserManager(BaseUserManager):
    """
    Менеджер для CustomUser, который позволяет использовать email в качестве основного поля.
    """
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError('Email адрес должен быть указан')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):

        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Суперпользователь должен иметь is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Суперпользователь должен иметь is_superuser=True.')

        return self.create_user(email, password, **extra_fields)

class CustomUser(AbstractBaseUser, PermissionsMixin):
    """
    Пользовательская модель пользователя, расширяющая AbstractBaseUser Django.
    Использует email в качестве основного уникального идентификатора для входа.
    """
    email = models.EmailField(unique=True, verbose_name='Email адрес')
    phone_number = models.CharField(max_length=15, blank=True, null=True, verbose_name='Номер телефона')
    avatar = models.ImageField(upload_to='avatars/', blank=True, null=True, verbose_name='Аватар')


    first_name = models.CharField(max_length=30, blank=True, verbose_name='Имя')
    last_name = models.CharField(max_length=30, blank=True, verbose_name='Фамилия')
    is_staff = models.BooleanField(default=False, verbose_name='Статус персонала')
    is_active = models.BooleanField(default=True, verbose_name='Активен')
    date_joined = models.DateTimeField(default=timezone.now, verbose_name='Дата регистрации')


    groups = models.ManyToManyField(
        'auth.Group',
        blank=True,
        help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.',
        related_name="customuser_set", # Важно для избежания конфликтов related_name
        related_query_name="customuser",
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        blank=True,
        help_text='Specific permissions for this user.',
        related_name="customuser_set", # Важно для избежания конфликтов related_name
        related_query_name="customuser",
    )

    objects = CustomUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.email

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'