from django.contrib import admin
from django.urls import path, include 

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('fruits.urls')),  # Подключение URLs из приложения fruits
]
