from django.urls import path
from django.contrib.auth import views as auth_views
from .views import (
    UserRegistrationView,
    ClientUserRegistrationView,
    ProfessionalUserRegistrationView,
    HomeListView,
    ProfileView,
    CatagoryDetailView,
    UserUpdateView,
)

urlpatterns = [
    path('register/', UserRegistrationView.as_view(), name = 'register'),
    path('register/client/', ClientUserRegistrationView.as_view(), name = 'client-register'),
    path('register/professional/', ProfessionalUserRegistrationView.as_view(), name = 'professional-register'),
    path('', HomeListView.as_view(), name = 'home'),
    path('profile/', ProfileView.as_view(), name = 'profile'),
    path('catagory-detail/', CatagoryDetailView.as_view(), name = 'catagory-detail'),
    path('login/', auth_views.LoginView.as_view(template_name = 'users/login.html'), name = 'login'),
    path('logout/', auth_views.LogoutView.as_view(template_name = 'users/logout.html'), name = 'logout'),
    path('users/<int:pk>/update/', UserUpdateView.as_view(), name = 'user-update'),
]