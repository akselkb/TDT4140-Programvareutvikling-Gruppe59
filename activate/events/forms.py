from django import forms

from events.models import Activity


class CreateActivityForm(forms.ModelForm):
    title = forms.CharField(label='Tittel', max_length=200)
    text = forms.CharField(label='Beskrivelse', widget=forms.Textarea())
    date_from = forms.DateTimeField(label='Fra dato', help_text='Eks: 2012-04-18 11:01')
    date_to = forms.DateTimeField(label='Til dato', help_text='Eks: 2012-04-18 11:01')
    gear = forms.CharField(label='Utstyr', max_length=200, required=False, help_text='Optional')

    class Meta:
        model = Activity
        fields = ('title', 'text', 'date_from', 'date_to', 'gear')
