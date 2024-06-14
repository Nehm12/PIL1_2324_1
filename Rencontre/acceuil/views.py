from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request, 'templates/index.html')

def blog(request):
    return render(request, 'templates/blog.html')

def contact(request):
    return render(request, 'templates/contact.html')

def about(request):
    return render(request, 'templates/about.html')