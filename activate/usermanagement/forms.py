from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Profile
import datetime


class SignUpForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, required=False, help_text='Valgfri.')
    last_name = forms.CharField(max_length=30, required=False, help_text='Valgfri.')
    birth_date = forms.DateField(label='Fødselsdato',
                                 widget=forms.SelectDateWidget
                                 (years=[x for x in range(1970, datetime.datetime.now().year)]),
                                 required=False, help_text='Valgfri.')
    email = forms.EmailField(max_length=254, help_text='Påkrevet. Skriv inn en gyldig email-adresse.')

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'birth_date', 'email', 'password1', 'password2',)


class UserUpdateForm(forms.ModelForm):
    first_name = forms.CharField(max_length=30, required=False, help_text='Valgfri.')
    last_name = forms.CharField(max_length=30, required=False, help_text='Valgfri.')
    birth_date = forms.DateField(label='Fødselsdato',
                                 widget=forms.SelectDateWidget
                                 (years=[x for x in range(1970, datetime.datetime.now().year)]),
                                 required=False, help_text='Valgfri.')
    email = forms.EmailField(max_length=254, help_text='Påkrevet. Skriv inn en gyldig email-adresse.')

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'birth_date', 'email']


class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = []
