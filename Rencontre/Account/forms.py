from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import get_user_model
from Account.models import UserInterest
from .models import UserProfile
User = get_user_model()


class SignUpForm(UserCreationForm):
    email = forms.EmailField()
    gender_choices = [('homme', 'Homme'), ('femme', 'Femme'), ('autre', 'Autre')]
    orientation_choices = [
        ('hetero', 'Hétérosexuel'),
        ('homosexuel', 'Homosexuel'),
        ('asexuel', 'Asexuel'),
        ('bisexuel', 'Bisexuel'),
        ('pansexuel', 'Pansexuel'),
        ('queer', 'Queer'),
    ]
    marital_status_choices = [
        ('celibataire', 'Célibataire'),
        ('marie', 'Marié(e)'),
        ('veuf', 'Veuf(ve)'),
        ('divorce', 'Divorcé(e)'),
    ]

    gender = forms.ChoiceField(choices=gender_choices)
    orientation = forms.ChoiceField(choices=orientation_choices)
    birth_year = forms.IntegerField(label='Année de naissance', min_value=1900, max_value=2006)
    country = forms.CharField(label='Pays d\'origine', max_length=100)
    marital_status = forms.ChoiceField(choices=marital_status_choices)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2', 'gender', 'orientation', 'birth_year', 'country', 'marital_status']
   
    def clean(self):
        cleaned_data = super().clean()
        password1 = cleaned_data.get("password1")
        password2 = cleaned_data.get("password2")

        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Les mots de passe ne correspondent pas.")
        
        return cleaned_data
    
    
    
    def save(self, commit=True):
        user = super().save(commit=False)
        user.email = self.cleaned_data.get('email')
        user.set_password(self.cleaned_data['password'])
        if commit:
            user.save()

            User_Profile = UserProfile.objects.create(
                user=user,
                gender=self.cleaned_data.get('gender'),
                orientation=self.cleaned_data.get('orientation'),
                birth_year=self.cleaned_data.get('birth_year'),
                country=self.cleaned_data.get('country'),
                marital_status=self.cleaned_data.get('marital_status')
            )
        return user



class LoginForm(forms.Form):
    username = forms.CharField(max_length=150)
    password = forms.CharField(widget=forms.PasswordInput)
    remember_me = forms.BooleanField(required=False)

class CustomAuthenticationForm(AuthenticationForm):
    remember_me = forms.BooleanField(required=False)

class InterestForm(forms.Form):
    INTEREST_CHOICES = [
        ('Musique', 'Music'),
        ('Sport', 'Sport'),
        ('Voyage', 'Travels'),
        ('Lecture', 'Novel'),
        ('Cinéma', 'Cinema'),
        ('Jeux Vidéo', 'Video Game'),
        ('Cuisine', 'Cook'),
        ('Technologie', 'Technology'),
        ('Art', 'Arts'),
        ('Photographie', 'Photography'),
    ]

    interests = forms.MultipleChoiceField(
        choices=INTEREST_CHOICES,
        widget=forms.CheckboxSelectMultiple(attrs={'class': 'interest'})
    )



