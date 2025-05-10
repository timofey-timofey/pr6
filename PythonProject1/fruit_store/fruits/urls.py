from django.urls import path
from . import views

urlpatterns = [
    path('', views.fruit_list, name='fruit_list'),
    path('add/', views.add_fruit, name='add_fruit'),
    path('delete/<int:fruit_id>/', views.delete_fruit, name='delete_fruit'),
]