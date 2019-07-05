from django.contrib.auth import login, authenticate
from .forms import UserRegistrationFrom, ClientUserRegistrationFrom, ProfessionalUserRegistrationFrom, ProfessionalUserProfileUpdateForm
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.shortcuts import render, redirect
from django.views.generic.edit import FormView
from django.views.generic import ListView, UpdateView, DetailView
from .models import BaseUser, ClientUser, ProfessionalUser
from django.conf import settings
from django.contrib.auth import get_user_model  

from .models import BaseUser
from django.urls import reverse_lazy

class UserRegistrationView(FormView):
    form_class = UserRegistrationFrom
    template_name = 'users/register.html'

    def form_valid(self, form):
        form.save()
        username = form.cleaned_data.get('username')
        raw_password = form.cleaned_data.get('password1')
        user = authenticate(username = username, password = raw_password)
        login(self.request, user)
        return redirect('profile:home')


class ClientUserRegistrationView(FormView):
    model = BaseUser
    form_class = ClientUserRegistrationFrom
    template_name = 'users/client_register.html'

    def form_valid(self, form):
        user = form.save()
        user.is_client = True
        user.save()
        client = ClientUser.objects.create(user=user)
        client.save()
        login(self.request, user)
        return redirect('profile:home')


class ProfessionalUserRegistrationView(FormView):
    model = BaseUser
    form_class = ProfessionalUserRegistrationFrom
    template_name = 'users/professional_register.html'
    # def get_context_data(self, **kwargs):
    #     kwargs['user_type'] = 'professional'
    #     return super().get_context_data(**kwargs)
    def form_valid(self, form):
        print("hello")
        user = form.save()
        user.is_professional = True
        x = form.cleaned_data['professional_license']
        y = form.cleaned_data['area_of_expertise']
        z = form.cleaned_data['hospital']
        user.save()
        professional = ProfessionalUser.objects.create(user=user, professional_license=x, area_of_expertise=y, hospital=z)
        professional.save()
        login(self.request, user)
        return redirect('profile:home')


class HomeListView(LoginRequiredMixin, ListView):
    model = BaseUser
    login_url = '/'
    template_name = 'users/home.html'


class ProfileView(LoginRequiredMixin, DetailView):
    model = ProfessionalUser
    login_url = '/'
    template_name = 'users/profile.html'

    # def get_context_data(self, **kwargs):
    #     context = super(ProfileView, self).get_context_data(**kwargs)
    #     context['expertise_type'] = ProfessionalUser.objects.all()
    #     return context
        # success_url = reverse_lazy('profile', kwargs={'pk': self.object.pk})
    


class CatagoryDetailView(LoginRequiredMixin, ListView):
    model = BaseUser
    login_url = '/'
    template_name = 'users/catagory_detail.html'


class UserUpdateView(UpdateView):
    model = BaseUser
    form_class = ProfessionalUserProfileUpdateForm
    template_name = 'users/user_detail_update.html'
    success_url = reverse_lazy('profile:home')