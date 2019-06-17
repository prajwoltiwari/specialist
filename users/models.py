from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.conf import settings
from PIL import Image

# Create your models here.
class MyUserManager(BaseUserManager):
    def create_user(self, email, date_of_birth, password=None):
        if not email:
            raise ValueError('Users must have an email address')
        user = self.model(
            email=self.normalize_email(email),
            date_of_birth=date_of_birth,
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, date_of_birth, password):
        user = self.create_user(
            email,
            password=password,
            date_of_birth=date_of_birth,
        )
        user.is_admin = True
        user.save(using=self._db)
        return user

class BaseUser(AbstractUser):
    fullname = models.CharField(max_length=100, unique = True)
    address = models.CharField(max_length=100)
    phone_number = models.IntegerField(null=True)
    email_address = models.EmailField()
    image = models.ImageField(default='default_profile_picture.jpg', upload_to='project_pics')

    objects = MyUserManager()

    USERNAME_FIELD = 'fullname'
    REQUIRED_FIELDS = ['address', 'email_address']

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
    is_client = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.user.username} Client'

class ProfessionalUser(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name = 'professional', primary_key=True)
    is_professional = models.BooleanField(default=False)
    AREA_OF_EXPERTISE_CHOICE = (
        ('doctor', 'doctor'),
        ('lawyer', 'lawyer'),
        ('therapist', 'therapist'),
        ('personal_trainer', 'personal_trainer'),
        ('home_tuition', 'home_tuition'),
        ('programmer', 'programmer')
    )
    area_of_expertise = models.CharField(max_length=20, choices=AREA_OF_EXPERTISE_CHOICE, default=None)
    area_of_specialization = models.TextField(blank=True)
    professional_license = models.FileField(upload_to='license_files')

    def __str__(self):
        return f'{self.user.username} Professional'


# class ClientProfile(models.Model):
#     client_profile = models.OneToOneField(ClientUser, on_delete=models.CASCADE)

#     def __str__(self):
#         return f'{self.user.username} Client Profile'



# class ProfessionalProfile(models.Model):
#     professional_profile = models.OneToOneField(ProfessionalUser, on_delete=models.CASCADE)

#     def __str__(self):
#         return f'{self.user.username} Professional Profile'