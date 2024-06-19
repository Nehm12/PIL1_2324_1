# forms.py
from django import forms
from Account.models import Interest

class FilterForm(forms.Form):
    age_min = forms.IntegerField(label='Âge minimum', required=False)
    age_max = forms.IntegerField(label='Âge maximum', required=False)
    gender = forms.ChoiceField(label='Genre', choices=Interest.GENDER_CHOICES, required=False)
    location = forms.CharField(label='Localisation', required=False)


class SearchForm(forms.Form):
    search = forms.CharField(label='Rechercher', max_length=100, required=False)
    gender = forms.ChoiceField(label='Genre', choices=[('', 'Tous')] + Interest.GENDER_CHOICES, required=False)
    age_min = forms.IntegerField(label='Âge minimum', required=False)
    age_max = forms.IntegerField(label='Âge maximum', required=False)
    location = forms.CharField(label='Localisation', required=False)
