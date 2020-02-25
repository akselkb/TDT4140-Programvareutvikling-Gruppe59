from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Profile
import datetime


class SignUpForm(UserCreationForm):
    email = forms.EmailField(max_length=254, required=True, help_text='Påkrevet. Skriv inn en gyldig email-adresse.')

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2',)


class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField(max_length=254, help_text='Påkrevet. Skriv inn en gyldig email-adresse.')

    class Meta:
        model = User
        fields = ['username', 'email']


class ProfileUpdateForm(forms.ModelForm):
    first_name = forms.CharField(max_length=30, help_text='Valgfri.', required=False)
    last_name = forms.CharField(max_length=30, help_text='Valgfri.', required=False)
    birth_date = forms.DateField(label='Fødselsdato',
                                 widget=forms.SelectDateWidget
                                 (years=[x for x in range(1970, datetime.datetime.now().year+1)]),
                                 help_text='Valgfri.', required=False)

    class Meta:
        model = Profile
        fields = ['first_name', 'last_name', 'birth_date']
