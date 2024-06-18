# your_project/urls.py
from django.contrib import admin
from django.urls import include, path
from Account import views
from django.views.generic import TemplateView

urlpatterns = [
    path('admin/', admin.site.urls), 
    path('', TemplateView.as_view(template_name='index.html'), name='home'),
    path('blog/', TemplateView.as_view(template_name='blog.html'), name='blog'),
    path('contact/', TemplateView.as_view(template_name='contact.html'), name='contact'),
    path('about/', TemplateView.as_view(template_name='about.html'), name='about'),
    path('Account/', include('Account.urls')),

    # Ajouter d'autres URLs ici si nécessaire

]





