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
    path('chat', views.rt, name='rt'),
    path('Suggest/', views.sug, name='gtsug'),
    path('edit_profile/', views.edit_profile, name='edit_profile'),
    
    path('reset_password/', v.PasswordResetView.as_view(), name='reset_password'),
    path('reset_password_send',v.PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('reset/<uid64>/<token>',v.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('reset_password_complete', v.PasswordResetCompleteView.as_view(),name='password_reset_complete')
]