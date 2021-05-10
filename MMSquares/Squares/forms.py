from os import X_OK
from random import choices
from crispy_forms.layout import Layout, Submit
from crispy_forms.bootstrap import FieldWithButtons, StrictButton
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms.models import ModelChoiceField
from django.forms.widgets import PasswordInput
from .models import SquaresCSV, Players
from crispy_forms.helper import FormHelper


class LoginForm(forms.Form):
    username = forms.CharField(max_length=10, widget = forms.TextInput(attrs={'autofocus': 'autofocus'}))
    password = forms.CharField(widget=PasswordInput())


class UploadCSVForm(forms.ModelForm):
    class Meta:
        model = SquaresCSV
        fields = ['file']
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['file'].label = ''


class WinnerForm(forms.Form):
    # This is to change the labels of the 'winner' drop down in the WinnerForm
    class NameChoiceField(ModelChoiceField):
        def label_from_instance(self, obj):
            return f'{obj.player}'

    ROUND_CHOICES = [
        ('first_round', 'First Round'),
        ('second_round', 'Second Round'),
        ('sweet_sixteen', 'Sweet 16'),
        ('elite_eight','Elite Eight'),
        ('final_four', 'Final Four'),
        ('championship', 'Championship'),
    ]
    # Get all players and put into a choice field
    winner = NameChoiceField(queryset=Players.objects.all())
    # Get all six rounds into a choice field
    round_number = forms.ChoiceField(choices=ROUND_CHOICES)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_show_labels = False