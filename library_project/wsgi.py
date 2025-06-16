"""
Конфигурация WSGI для проекта library_project.

Этот файл предоставляет вызываемый объект WSGI как переменную уровня модуля с именем ``application``.

Дополнительную информацию об этом файле см. на странице
https://docs.djangoproject.com/en/5.2/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'library_project.settings')

application = get_wsgi_application()
