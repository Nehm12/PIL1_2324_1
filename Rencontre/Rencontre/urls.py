# your_project/urls.py
from django.contrib import admin
from django.urls import path
from Account import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('signup/', views.signup, name='signup'),
    path('login/', views.login_view, name='login'),
    path('', views.home, name='home'),  # assuming you have a home view
]
