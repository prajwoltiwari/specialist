from django.contrib.auth import login, authenticate
from .forms import UserRegistrationFrom, UserDetailUpdateForm, ClientUserRegistrationFrom, ProfessionalUserRegistrationFrom
from django.shortcuts import render, redirect
from django.views.generic.edit import FormView
from django.views.generic import ListView, UpdateView
from .models import BaseUser
from django.urls import reverse_lazy

class UserRegistrationView(FormView):
    form_class = UserRegistrationFrom
    template_name = 'users/register.html'

    def form_valid(self, form):
        form.save()
        # a=AdminUser.objects.create(user=user,is-client=True)
        username = form.cleaned_data.get('username')
        raw_password = form.cleaned_data.get('password1')
        user = authenticate(username = username, password = 'password1')
        login(self.request, user)
        return redirect('home')


class ClientUserRegistrationView(FormView):
    model = BaseUser
    form_class = ClientUserRegistrationFrom
    template_name = 'users/client_register.html'

    def get_context_data(self, **kwargs):
        kwargs['user_type'] = 'client'
        return super().get_context_data(**kwargs)

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('home')


class ProfessionalUserRegistrationView(FormView):
    model = BaseUser
    form_class = ProfessionalUserRegistrationFrom'
    template_name = 'users/professional_register.html'

    def get_context_data(self, **kwargs):
        kwargs['user_type'] = 'professional'
        return super().get_context_data(**kwargs)

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('home')


class HomeListView(ListView):
    model = BaseUser
    template_name = 'users/home.html'


class UserUpdateView(UpdateView):
    model = BaseUser
    form_class = UserDetailUpdateForm
    template_name = 'users/user_detail_update.html'
    success_url = reverse_lazy('home')