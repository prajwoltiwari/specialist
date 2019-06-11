from django.contrib import admin
from .models import BaseUser, ClientUser, ProfessionalUser

# Register your models here.

admin.site.register(BaseUser)
admin.site.register(ClientUser)     
admin.site.register(ProfessionalUser)     