from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import BaseUser

class UserRegistrationFrom(UserCreationForm):
    first_name = forms.CharField(max_length = 30, required = False, help_text = 'Optional')
    last_name = forms.CharField(max_length = 30, required = False, help_text = 'Optional')
    email = forms.EmailField(max_length = 256, help_text = 'Required Field. Please enter a valid email address.')

    class meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2',)


class UserDetailUpdateForm(forms.ModelForm):
    class Meta:
        model = BaseUser
        fields = [
            'fullname',
            'address',
            'image',
        ]