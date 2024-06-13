from django.contrib import admin
from django.urls import path,include
from . import views
from django.contrib.auth import views as v
#from django.shortcuts import redirect



urlpatterns = [
    path('', views.acc, name='acc'),
    path('inscription/',views.ins, name='ins'),
    path('search/',views.search_user, name='sea'),
    path('login/',v.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/',v.LogoutView.as_view(template_name='logout.html',next_page='acc'), name='logout'),
    path('acceuil', views.acceuil, name='acl'),
    #path('Sugestions/', views.suggest_users, name='sug'),

]