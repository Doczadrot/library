"""
Главный URL-конфиг проекта
Определяет маршруты административной панели
"""
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('library.urls', namespace='library')),
    path('users/', include('users.urls', namespace='users')),
]
