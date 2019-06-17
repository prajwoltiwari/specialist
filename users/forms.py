from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import BaseUser
from django.contrib.auth import get_user_model


class UserRegistrationFrom(UserCreationForm):
    first_name = forms.CharField(max_length = 30, required = False, help_text = 'Optional')
    last_name = forms.CharField(max_length = 30, required = False, help_text = 'Optional')
    email = forms.EmailField(max_length = 256, help_text = 'Required Field. Please enter a valid email address.')

    class Meta:
        model = get_user_model()
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2',)


class UserDetailUpdateForm(forms.ModelForm):
    class Meta:
        model = get_user_model()
        fields = [
            'fullname',
            'address',
            'image',
        ]