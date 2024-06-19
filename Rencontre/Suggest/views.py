# from django.shortcuts import render
# from django.shortcuts import render, redirect
# # from .forms import UserForm, ProfileForm, InterestForm
# from django.contrib.auth import login
# # from django.contrib.auth.models import User
# # from django.core.paginator import Paginator
# from Account.models import Interest, Profile
# from django.db.models import Min, Max 
# # Create your views here.
# def suggest_users(request):
#     user_profile = Profile.objects.get(user=request.user)
    
#     # Récupérer les intérêts de l'utilisateur connecté
#     user_interests = user_profile.interests.all()

#     # Récupérer les critères des intérêts
#     genders = user_interests.values_list('gender', flat=True)
#     # if user_profile.sexe == 'F':
#     #      genders='M'
#     # else:
#     #     genders='F'
    
#     min_age = user_interests.aggregate(Min('min_age'))['min_age__min']
#     max_age = user_interests.aggregate(Max('max_age'))['max_age__max']
#     location = user_profile.location
#     sexe= user_profile.sexe
#     # Rechercher les profils correspondant aux critères
#     suggested_profiles = Profile.objects.filter(
#         age__gte=min_age,
#         age__lte=max_age,
#         # location=location, 
#         interests__gender__in=sexe 
#     ).exclude(user=user_profile.user).distinct()

#     return render(request, 'sugest.html', {'suggested_profiles': suggested_profiles})

# views.py
from django.contrib.auth.models import User
from django.core.paginator import Paginator
from django.shortcuts import render, redirect
from Account.models import Interest, Profile
from .forms import FilterForm
from django.db.models import Min, Max
from django.contrib.auth.decorators import login_required
from .forms import SearchForm
@login_required
def suggest_users(request):
    user_profile = Profile.objects.get(user=request.user)
    
    # Récupérer les intérêts de l'utilisateur connecté
    user_interests = user_profile.interests.all()
    
    # Initialiser les critères par défaut
    min_age = user_interests.aggregate(Min('min_age'))['min_age__min'] or 18  # valeur par défaut si None
    max_age = user_interests.aggregate(Max('max_age'))['max_age__max'] or 100  # valeur par défaut si None
    sexe = user_profile.sexe or 'M'
    s= request.GET.get('gender','')
    location = user_profile.location or ''
    
    # Traitement du formulaire de filtre
    if request.method == 'GET':
        form = FilterForm(request.GET)
        if form.is_valid():
            age_min = form.cleaned_data.get('age_min') or min_age
            age_max = form.cleaned_data.get('age_max') or max_age
            gender = form.cleaned_data.get('gender') or request.GET.get('gender','')
            location = form.cleaned_data.get('location') or location
        else:
            age_min = min_age
            age_max = max_age
            gender = s
            location = location
    else:
        form = FilterForm()
        age_min = min_age
        age_max = max_age
        gender = s
        location = location
    
    # Rechercher les profils correspondant aux critères
    suggested_profiles = Profile.objects.filter(
        age__gte=age_min,
        age__lte=age_max,
        # location__icontains=location,
        sexe__in=s
    ).exclude(user=user_profile.user).distinct()
    
    return render(request, 'sugest.html', {'suggested_profiles': suggested_profiles, 'form': form})



# def search_user(request):
#     search = request.GET.get('search', '')
#     us = User.objects.filter(username__icontains=search)
#     paginator = Paginator(us, 3)
#     page_number = request.GET.get('page')
#     page_obj = paginator.get_page(page_number)
    
#     context = {
#         'us': page_obj
#     }
#     return render(request, 'search.html', context)

# views.py


# @login_required
# def search_user(request):
#     search = request.GET.get('search', '')
#     us = User.objects.filter(username__icontains=search)
    
#     context = {
#         'us': us,
#         'search': search,
#     }
#     return render(request, 'search.html', context)


# views.py


@login_required
def search_user(request):
    search = request.GET.get('search', '')
    gender_filter = request.GET.get('gender', '')
    age_min_filter = request.GET.get('age_min', '')
    age_max_filter = request.GET.get('age_max', '')
    location_filter = request.GET.get('location', '')

    us = User.objects.filter(username__icontains=search).exclude(id=request.user.id)
    
    
    if gender_filter:
        us = us.filter(profile__interests__gender=gender_filter)
    
    if age_min_filter:
        us = us.filter(profile__age__gte=age_min_filter)
    
    
    if age_max_filter:
        us = us.filter(profile__age__lte=age_max_filter)
    
    
    if location_filter:
        us = us.filter(profile__location__icontains=location_filter)
    
    
    context = {
        'us': us,
        'search': search,
        'gender_filter': gender_filter,
        'age_min_filter': age_min_filter,
        'age_max_filter': age_max_filter,
        'location_filter': location_filter
    }
    return render(request, 'search.html', context)
