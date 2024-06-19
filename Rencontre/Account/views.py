from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate
from django.urls import reverse
from django.contrib.auth.forms import PasswordResetForm
from django.contrib import messages

from Account.models import UserInterest, UserProfile
from .forms import SignUpForm, User 
from django.contrib.auth.views import PasswordResetView, PasswordResetConfirmView
from django.urls import reverse_lazy

def signup_view(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            # Créer un nouvel utilisateur avec les données du formulaire
              # Utilisation de la méthode save personnalisée du formulaire
            user = form.save(commit=True)
            # Redirection vers la page de connexion après inscription réussie
            return redirect('login')
    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form': form})



@login_required
def select_interests_view(request):
    return render(request, 'select_interests.html')




class CustomPasswordResetView(PasswordResetView):
    template_name = 'registration/password_reset_form.html'
    email_template_name = 'registration/password_reset_email.html'
    success_url = reverse_lazy('password_reset_done')

class CustomPasswordResetConfirmView(PasswordResetConfirmView):
    template_name = 'registration/password_reset_confirm.html'
    success_url = reverse_lazy('password_reset_complete')


























