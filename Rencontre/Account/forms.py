from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import get_user_model
User = get_user_model()


class SignUpForm(forms.ModelForm):
    username = forms.CharField(max_length=150)
    password = forms.CharField(widget=forms.PasswordInput)
    re_password = forms.CharField(label='Re-type Password', widget=forms.PasswordInput)
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
        fields = ['username', 'email', 'password', 're_password', 'gender', 'orientation', 'birth_year', 'country', 'marital_status']


    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get('password')
        re_password = cleaned_data.get('re_password')

        if password != re_password:
            raise forms.ValidationError("Les mots de passe ne correspondent pas")

class LoginForm(forms.Form):
    username = forms.CharField(max_length=150)
    password = forms.CharField(widget=forms.PasswordInput)
    remember_me = forms.BooleanField(required=False)

class CustomAuthenticationForm(AuthenticationForm):
    remember_me = forms.BooleanField(required=False)


