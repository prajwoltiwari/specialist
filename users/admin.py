from django.contrib import admin
from .models import BaseUser, Client

# Register your models here.

admin.site.register(BaseUser)
admin.site.register(Client)     