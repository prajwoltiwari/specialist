from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import BaseUser, ClientUser, ProfessionalUser
from django.contrib.auth import get_user_model
from django.db import transaction


class UserRegistrationFrom(UserCreationForm):
    first_name = forms.CharField(max_length = 30, required = False)
    last_name = forms.CharField(max_length = 30, required = False)
    email = forms.EmailField(max_length = 256)

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
        
    def __init__(self, *args, **kwargs):
        super(ClientUserRegistrationFrom, self).__init__(*args, **kwargs)
        self.fields['password1'].help_text = ''
        self.fields['password2'].help_text = ''
        self.fields['username'].help_text = ''


class ProfessionalUserRegistrationFrom(UserCreationForm):
    # first_name = forms.CharField(max_length = 30, required = False, help_text = 'Optional')
    # last_name = forms.CharField(max_length = 30, required = False, help_text = 'Optional')
    # email = forms.EmailField(max_length = 256, help_text = 'Required Field. Please enter a valid email address.')
    # fullname = forms.CharField(max_length = 30, required = False, help_text = 'Optional')
    # email = forms.EmailField(max_length = 256, help_text = 'Required Field. Please enter a valid email address.')
    AREA_OF_EXPERTISE_CHOICE = (
        ('doctor', 'doctor'),
        ('lawyer', 'lawyer'),
        ('therapist', 'therapist'),
        ('personal_trainer', 'personal_trainer'),
        ('home_tuition', 'home_tuition'),
        ('programmer', 'programmer')
    )
    area_of_expertise = forms.ChoiceField(choices = AREA_OF_EXPERTISE_CHOICE)
    professional_license = forms.ImageField(required = True)
    
    class Meta:
        model = get_user_model()
        fields = ('username', 'email', 'password1', 'password2', 'area_of_expertise', 'professional_license')

    def __init__(self, *args, **kwargs):
        super(ProfessionalUserRegistrationFrom, self).__init__(*args, **kwargs)
        self.fields['password1'].help_text = ''
        self.fields['password2'].help_text = ''
        self.fields['username'].help_text = ''
        
    # @transaction.atomic
    # def save(self):
    #     user = super().save(commit=False)
    #     user.is_professional = True
    #     user.save()
    #     professional = ProfessionalUser.objects.create(user=user)
    #     professional.area_of_expertise.add(self.cleaned_data.get('area_of_expertise'))
    #     professional.area_of_specialization.add(self.cleaned_data.get('area_of_specialization'))
    #     professional.professional_license.add(self.cleaned_data.get('professional_license'))


class ProfessionalUserProfileUpdateForm(forms.ModelForm):
    fullname = forms.CharField(required=False)
    hospital_address = forms.CharField(required=False)
    phone_number = forms.IntegerField(required=False)
    description = forms.TextInput()
    image = forms.ImageField(required=False)