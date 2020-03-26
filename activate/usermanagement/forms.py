from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Profile
import datetime


class SignUpForm(UserCreationForm):
    first_name = forms.CharField(label='Fornavn', max_length=30, required=True, help_text='Påkrevet.')
    last_name = forms.CharField(label='Etternavn', max_length=30, required=True, help_text='Påkrevet.')
    email = forms.EmailField(max_length=254, required=True, help_text='Påkrevet. Skriv inn en gyldig email-adresse.')

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2',)


class UserUpdateForm(forms.ModelForm):
    first_name = forms.CharField(label='Fornavn', max_length=30, required=True, help_text='Påkrevet.')
    last_name = forms.CharField(label='Etternavn', max_length=30, required=True, help_text='Påkrevet.')
    email = forms.EmailField(max_length=254, help_text='Påkrevet. Skriv inn en gyldig email-adresse.')


    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email']


class ProfileUpdateForm(forms.ModelForm):
    birth_date = forms.DateField(label='Fødselsdato',
                                 widget=forms.SelectDateWidget
                                 (years=[x for x in range(1970, datetime.datetime.now().year+1)]),
                                 required=False, help_text='Valgfri.')
    image = forms.ImageField(label='Profilbilde', allow_empty_file=True)

    class Meta:
        model = Profile
        fields = ['birth_date', 'image', 'NTNUI_medlem', 'anonymous']
