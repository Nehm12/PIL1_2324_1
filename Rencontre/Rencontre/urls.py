# your_project/urls.py
from django.contrib import admin
from django.urls import include, path
from Account import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),  
    path('blog/', include('acceuil.urls')),
    path('contact/', include('acceuil.urls')),
    path('about/', include('acceuil.urls')),
    path('signup/', views.signup, name='signup'),
    path('login/', views.login_view, name='login'),
    # assuming you have a home view
]
