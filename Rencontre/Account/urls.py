from django.urls import include, path
from django.contrib import admin
from .views import signup_view, login_view

urlpatterns = [
     path('admin/', admin.site.urls),
    path('signup/', signup_view, name='signup'),
    path('login/', login_view, name='login'),
]
