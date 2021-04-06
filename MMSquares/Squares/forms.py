from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms.widgets import PasswordInput
from django import forms
from .models import SquaresCSV


class RegisterForm(UserCreationForm):
    username = forms.CharField(max_length=10, required=True, help_text='This is only for the admin.', widget=forms.TextInput(attrs={'autofocus': 'autofocus'}))

    class Meta:
        model = User
        fields = ('first_name', 'username', 'password1', 'password2')



class LoginForm(forms.Form):
    initials = forms.CharField(max_length=10, widget = forms.TextInput(attrs={'autofocus': 'autofocus'}))
    password = forms.CharField(widget=PasswordInput())


class UploadCSVForm(forms.ModelForm):

    class Meta:
        model = SquaresCSV
        fields = ['file']