# chat/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('private/<str:username>/', views.private_chat, name='private_chat'),
    path('', views.user_list, name='user_list'),
]
