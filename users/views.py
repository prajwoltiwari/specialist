from django.contrib.auth import login, authenticate
from .forms import UserRegistrationFrom, UserDetailUpdateForm
from django.shortcuts import render, redirect
from django.views.generic.edit import FormView
from django.views.generic import ListView, UpdateView
from .models import BaseUser
from django.urls import reverse

class UserRegistrationView(FormView):
    form_class = UserRegistrationFrom
    template_name = 'register.html'

    def form_valid(self, form):
        form.save()
        username = form.cleaned_data.get('username')
        raw_password = form.cleaned_data.get('password1')
        user = authenticate(username = username, password = 'password1')
        login(self.request, user)
        return redirect('home')


class HomeListView(ListView):
    model = BaseUser
    template_name = 'users/home.html'


class UserUpdateView(UpdateView):
    model = BaseUser
    form_class = UserDetailUpdateForm
    template_name = 'users/user-update'
    success_url = reverse('home')