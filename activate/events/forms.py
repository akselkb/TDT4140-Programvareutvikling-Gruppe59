from django import forms


class CreateActivityForm(forms.Form):
    title = forms.CharField(label='Tittel', max_length=200)
    text = forms.CharField(label='Beskrivelse', widget=forms.Textarea())
    date_from = forms.DateTimeField(label='Fra dato', help_text='Eks: 2012-04-18 11:01')
    date_to = forms.DateTimeField(label='Til dato', help_text='Eks: 2012-04-18 11:01')
