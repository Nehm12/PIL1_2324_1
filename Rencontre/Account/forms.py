from django import forms 
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Profile, Interest

class UserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['age','bio','sexe','location']
        
        # widgets = {, 'interests'
        #     'interests': forms.CheckboxSelectMultiple()
        # }

class InterestForm(forms.ModelForm):
    class Meta:
        model = Interest
        fields = ['gender', 'min_age', 'max_age','localisation']
        widgets = {
            'gender': forms.RadioSelect()
        }