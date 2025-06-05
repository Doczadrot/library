"""
Главный URL-конфиг проекта
Определяет маршруты административной панели
"""
from django.contrib import admin
from django.urls import path

urlpatterns = [
    path('admin/', admin.site.urls),
]
