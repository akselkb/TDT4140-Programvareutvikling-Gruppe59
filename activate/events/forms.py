from crispy_forms.bootstrap import FieldWithButtons, StrictButton
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Field, Div
from django import forms
import datetime

from .models import Activity


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
    price = forms.DecimalField(label='Pris', required=False, help_text='Valgfri.')

    show_email_address = forms.BooleanField(label='Vis e-post', required=False, help_text='Vis e-postadresse slik at deltakere kan ta kontakt.')
    krever_NTNUI_medlemskap = forms.CheckboxInput()

    class Meta:
        model = Activity
        fields = ('title', 'text', 'date', 'time_from', 'time_to', 'max_participants', 'gear', 'price', 'show_email_address', 'krever_NTNUI_medlemskap')


class SearchForm(forms.Form):
    query = forms.CharField(label='Søk', max_length=255, required=False)

    helper = FormHelper()
    helper.form_show_labels = False
    helper.help_text_inline = True
    helper.disable_csrf = True
    helper.layout = Layout(
        FieldWithButtons(
            Field('query', placeholder="Søk..."),
            StrictButton('<i class="fas fa-search"></i>', value='submit', type='submit', css_class='btn-primary')
        )
    )


class FilterForm(forms.Form):
    available = forms.BooleanField(label="Kun ledige", required=False)
    hide_ntnui = forms.BooleanField(label="Ikke NTNUI", required=False)
    free = forms.BooleanField(label="Kun gratis", required=False)

    helper = FormHelper()
    helper.disable_csrf = True
    helper.layout = Layout(
        Div(
            Field('available', type="checkbox", css_class="custom-control-input"),
            css_class="custom-control custom-switch pl-3"
        ),
        Div(
            Field('hide_ntnui', type="checkbox", css_class="custom-control-input"),
            css_class="custom-control custom-switch pl-3"
        ),
        Div(
            Field('free', type="checkbox", css_class="custom-control-input"),
            css_class="custom-control custom-switch pl-3"
        ),
        StrictButton('Filtrer', value='submit', type='submit', css_class='btn-primary')
    )


