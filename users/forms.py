from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import BaseUser, ClientUser, ProfessionalUser
from django.contrib.auth import get_user_model
from django.db import transaction


class UserRegistrationFrom(UserCreationForm):
    first_name = forms.CharField(max_length = 30, required = False, help_text = 'Optional')
    last_name = forms.CharField(max_length = 30, required = False, help_text = 'Optional')
    email = forms.EmailField(max_length = 256, help_text = 'Required Field. Please enter a valid email address.')

    class Meta:
        model = get_user_model()
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2',)


class ClientUserRegistrationFrom(UserCreationForm):
    # first_name = forms.CharField(max_length = 30, required = False, help_text = 'Optional')
    # last_name = forms.CharField(max_length = 30, required = False, help_text = 'Optional')
    # email = forms.EmailField(max_length = 256, help_text = 'Required Field. Please enter a valid email address.')
    class Meta:
        model = get_user_model()
        fields = ('username', 'email', 'password1', 'password2',)

    # @transaction.atomic
    def save(self):
        user = super().save(commit=False)
        user.is_client = True
        user.save()
        client = ClientUser.objects.create(user=user)


class ProfessionalUserRegistrationFrom(UserCreationForm):
    # first_name = forms.CharField(max_length = 30, required = False, help_text = 'Optional')
    # last_name = forms.CharField(max_length = 30, required = False, help_text = 'Optional')
    # email = forms.EmailField(max_length = 256, help_text = 'Required Field. Please enter a valid email address.')
    AREA_OF_EXPERTISE_CHOICE = (
        ('doctor', 'doctor'),
        ('lawyer', 'lawyer'),
        ('therapist', 'therapist'),
        ('personal_trainer', 'personal_trainer'),
        ('home_tuition', 'home_tuition'),
        ('programmer', 'programmer')
    )
    area_of_expertise = forms.CharField(max_length=20, choices=AREA_OF_EXPERTISE_CHOICE, default=None)
    area_of_specialization = forms.CharField(blank=True)
    professional_license = forms.FileField()
    class Meta:
        model = get_user_model()
        fields = ('username', 'email', 'password1', 'password2',)
        
    @transaction.atomic
    def save(self):
        user = super().save(commit=False)
        user.is_professional = True
        user.save()
        professional = ProfessionalUser.objects.create(user=user)
        professional.area_of_expertise.add(self.cleaned_data.get('area_of_expertise'))
        professional.area_of_specialization.add(self.cleaned_data.get('area_of_specialization'))
        professional.professional_license.add(self.cleaned_data.get('professional_license'))


class UserDetailUpdateForm(forms.ModelForm):
    class Meta:
        model = get_user_model()
        fields = [
            'fullname',
            'address',
            'image',
        ]