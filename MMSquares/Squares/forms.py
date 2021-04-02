from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms.widgets import PasswordInput
from django import forms
from .models import SquaresCSV


class RegisterForm(UserCreationForm):
    first_name = forms.CharField(max_length=20, required=True, widget = forms.TextInput(attrs={'autofocus': 'autofocus'}))
    username = forms.CharField(max_length=2, required=True, help_text='Set your initials as your username.')

    class Meta:
        model = User
        fields = ('first_name', 'username', 'password1', 'password2')



class LoginForm(forms.Form):
    initials = forms.CharField(max_length=2, widget = forms.TextInput(attrs={'autofocus': 'autofocus'}))
    password = forms.CharField(widget=PasswordInput())


class UploadCSVForm(forms.ModelForm):

    class Meta:
        model = SquaresCSV
        fields = ['file']