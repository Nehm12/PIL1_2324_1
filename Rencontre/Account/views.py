from django.shortcuts import render

# Create your views here.
<<<<<<< HEAD
=======
from django.shortcuts import render

# Create your views here.

from django.shortcuts import render, redirect
from .forms import UserForm, ProfileForm, InterestForm
from django.contrib.auth import login
from django.contrib.auth.models import User
from django.core.paginator import Paginator
from .models import Interest, Profile
from django.db.models import Min, Max 

def acc(request):
    return render(request, 'acc.html')

def ins(request):
    if request.method == 'POST':
        user_form = UserForm(request.POST)
        profile_form = ProfileForm(request.POST)
        interest_form = InterestForm(request.POST)

        if user_form.is_valid() and profile_form.is_valid() and interest_form.is_valid():
            user = user_form.save()
            
            profile = profile_form.save(commit=False)
            profile.user = user
            profile.save()
            
            # Manually adding many-to-many relations
            # profile_form.save_m2m()
            # profile.save()
            
            interest = interest_form.save()
            profile.interests.add(interest)
            
            
            login(request, user)
            return redirect('login')
        else:
            print(user_form.errors)
            print(profile_form.errors)
            print(interest_form.errors)
            
    else:
        user_form = UserForm()
        profile_form = ProfileForm()
        interest_form = InterestForm()

    context = {
        'user_form': user_form,
        'profile_form': profile_form,
        'interest_form': interest_form
    }
    
    return render(request, 'ins.html', context)

def search_user(request):
    search = request.GET.get('search', '')
    us = User.objects.filter(username__icontains=search)
    paginator = Paginator(us, 3)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    context = {
        'us': page_obj
    }
    return render(request, 'search.html', context)

def acceuil(request):
    return render(request, 'acco.html')




def suggest_users(request):
    user_profile = Profile.objects.get(user=request.user)
    
    # Récupérer les intérêts de l'utilisateur connecté
    user_interests = user_profile.interests.all()

    # Récupérer les critères des intérêts
    genders = user_interests.values_list('gender', flat=True)
    if genders == 'F':
         genders='M'
    else:
        genders='F'
    
    min_age = user_interests.aggregate(Min('min_age'))['min_age__min']
    max_age = user_interests.aggregate(Max('max_age'))['max_age__max']
    location = user_profile.location

    # Rechercher les profils correspondant aux critères
    suggested_profiles = Profile.objects.filter(
        age__gte=min_age,
        age__lte=max_age,
        # location=location, 
        interests__gender__in=genders
    ).exclude(user=user_profile.user).distinct()

    return render(request, 'sugest.html', {'suggested_profiles': suggested_profiles})
>>>>>>> origin/second
