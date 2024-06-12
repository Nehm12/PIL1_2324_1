from django.contrib import admin
from django.urls import path,include
from . import views

#from django.shortcuts import redirect



urlpatterns = [
    path('', views.suggest_users, name='sugs'),
    path('sugest/', views.suggest_users, name='suggest_users'),
    path('search/',views.search_user, name='sea'),
    # path('salle/<str:username>',views.room, name='salle')
    
]