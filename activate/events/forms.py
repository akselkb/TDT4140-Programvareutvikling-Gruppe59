from django import forms
import datetime

from events.models import Activity


class CreateActivityForm(forms.ModelForm):
    title = forms.CharField(label='Tittel', max_length=200)
    text = forms.CharField(label='Beskrivelse', widget=forms.Textarea())
    date = forms.DateField(label='Dato',
                           widget=forms.SelectDateWidget
                           (years=[x for x in range(datetime.datetime.now().year, datetime.datetime.now().year + 2)]),
                           required=False)
    time_from = forms.TimeField(label='Start tidspunkt', help_text='F.eks.: 16:30')
    time_to = forms.TimeField(label='Slutt tidspunkt', help_text='F.eks.: 18:00')

    max_participants = forms.IntegerField(label='Antall deltagere', required=False, help_text='Valgfri.')
    gear = forms.CharField(label='Utstyr', max_length=200, required=False, help_text='Valgfri.')

    show_email_address = forms.BooleanField(label='Vis e-post', required=False, help_text='Vis e-postadresse slik at deltakere kan ta kontakt.')

    class Meta:
        model = Activity
        fields = ('title', 'text', 'date', 'time_from', 'time_to', 'max_participants', 'gear', 'show_email_address')
