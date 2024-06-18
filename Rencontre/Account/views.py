from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.urls import reverse
from .forms import SignUpForm, LoginForm

def signup_view(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('login')  # Redirection vers la page de connexion
    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form': form})


def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                if user.is_superuser:
                    return redirect(reverse('admin:index'))  # Redirection vers la page d'administration
                else:
                    return redirect('home')  # Redirection vers la page d'accueil après connexion
            else:
                form.add_error(None, 'Nom d\'utilisateur ou mot de passe incorrect.')  # Message d'erreur personnalisé
        else:
            print(form.errors)  # Affichez les erreurs de validation dans la console
    else:
        form = LoginForm()
    return render(request, 'login.html', {'form': form})

























