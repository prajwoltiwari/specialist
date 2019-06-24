from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.conf import settings
from PIL import Image

# Create your models here.
class MyUserManager(BaseUserManager):
    def _create_user(self, email, password, **extra_fields):
       """Create and save a User with the given email and password."""
       if not email:
           pass
       email = self.normalize_email(email)
       user = self.model(email=email, **extra_fields)
       user.set_password(password)
       user.save(using=self._db)

       return user

    def create_user(self, email, password=None, **extra_fields):
       """Create and save a regular User with the given email and password."""
       extra_fields.setdefault('is_staff', False)
       extra_fields.setdefault('is_superuser', False)
       return self._create_user(email, password, **extra_fields)

    def create_superuser(self, email, password, **extra_fields):
       extra_fields.setdefault('is_staff', True)
       extra_fields.setdefault('is_superuser', True)
       if extra_fields.get('is_staff') is not True:
           raise ValueError('Superuser must have is_staff=True.')
       if extra_fields.get('is_superuser') is not True:
           raise ValueError('Superuser must have is_superuser=True.')

       return self._create_user(email, password, **extra_fields)

class BaseUser(AbstractUser):
    fullname = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    phone_number = models.IntegerField(null=True)
    email_address = models.EmailField()
    phone_number = models.IntegerField(null=True)
    image = models.ImageField(default='default_profile_picture.jpg', upload_to='project_pics')

    is_client = models.BooleanField(default=False)
    is_professional = models.BooleanField(default=False)

    objects = MyUserManager()


    def __str__(self):
        return f'{self.username}'

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        img = Image.open(self.image.path)
        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.image.path)



class ClientUser(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name = 'client', primary_key=True)
    # is_client = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.user.username} Client'

class ProfessionalUser(models.Model):
    user = models.OneToOneField(BaseUser, on_delete=models.CASCADE, related_name = 'professional', primary_key=True)
    # is_professional = models.BooleanField(default=False)
    AREA_OF_EXPERTISE_CHOICE = (
        ('doctor', 'doctor'),
        ('lawyer', 'lawyer'),
        ('therapist', 'therapist'),
        ('personal_trainer', 'personal_trainer'),
        ('home_tuition', 'home_tuition'),
        ('programmer', 'programmer')
    )
    area_of_expertise = models.CharField(max_length=20, choices=AREA_OF_EXPERTISE_CHOICE, default='doctor')
    area_of_specialization = models.TextField(blank=True)
    professional_license = models.ImageField(upload_to='license_files')

    def __str__(self):
        return f'{self.user.username} Professional'