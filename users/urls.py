from django.urls import path
from .views import (
    UserRegistrationView,
    HomeListView,
    UserUpdateView,
)

urlpatterns = [
    path('register/', UserRegistrationView.as_view(), name = 'register'),
    path('', HomeListView.as_view(), name = 'home'),
    path('users/<int:pk>/update/', UserUpdateView.as_view(), name = 'user-update'),
]