from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms.widgets import PasswordInput
from django import forms
from .models import SquaresCSV


class LoginForm(forms.Form):
    username = forms.CharField(max_length=10, widget = forms.TextInput(attrs={'autofocus': 'autofocus'}))
    password = forms.CharField(widget=PasswordInput())


class UploadCSVForm(forms.ModelForm):

    class Meta:
        model = SquaresCSV
        fields = ['file']