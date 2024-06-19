from django.urls import include, path
from django.contrib import admin
from .views import signup_view
from django.contrib.auth import views as auth_views
from Account import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('signup/', signup_view, name='signup'),
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('select_interests/', views.select_interests_view, name='select_interests'),
    path('password_reset/', views.CustomPasswordResetView.as_view(), name='password_reset'),
    path('reset/<uidb64>/<token>/', views.CustomPasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    # Autres URLs de votre application
    # Autres URLs de votre application


]
