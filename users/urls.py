from django.urls import path
from .views import UserRegistrationView, HomeListView

urlpatterns = [
    path('register/', UserRegistrationView.as_view(), name = 'register'),
    path('', HomeListView.as_view(), name = 'home'),
]