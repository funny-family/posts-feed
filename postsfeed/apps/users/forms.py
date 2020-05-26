from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class UserSignUpForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = [
            'username', # this field should be exactly named like this!
            'email', # this field should be exactly named like this!
            'password1', # this field should be exactly named like this!
            'password2' # this field should be exactly named like this!
        ]