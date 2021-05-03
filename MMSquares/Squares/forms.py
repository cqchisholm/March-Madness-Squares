from os import X_OK
from random import choices
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms.widgets import PasswordInput
from django import forms
from .models import SquaresCSV, Players
from crispy_forms.helper import FormHelper


class LoginForm(forms.Form):
    username = forms.CharField(max_length=10, widget = forms.TextInput(attrs={'autofocus': 'autofocus'}))
    password = forms.CharField(widget=PasswordInput())


class UploadCSVForm(forms.ModelForm):
    class Meta:
        model = SquaresCSV
        fields = ['file']


class WinnerForm(forms.Form):
    ROUND_CHOICES = [
        ('first_round', 'First Round'),
        ('second_round', 'Second Round'),
        ('sweet_sixteen', 'Sweet 16'),
        ('elite_eight','Elite Eight'),
        ('final_four', 'Final Four'),
        ('championship', 'Championship'),
    ]
    # Get list of players
    players = Players.objects.values_list('player', flat=True)
    WINNER_CHOICES = [(player, player) for player in players]
    # Get all six rounds into a choice field
    round_number = forms.ChoiceField(choices=ROUND_CHOICES)
    # Get all players and put into a choice field
    winner = forms.ChoiceField(choices=WINNER_CHOICES)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_show_labels = False