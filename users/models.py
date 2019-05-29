from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class BaseUser(AbstractUser):
    fullname = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    phone_number = models.IntegerField()
    email_address = models.EmailField()
    image = models.ImageField(default='default_profile_picture.jpg', upload_to='project_pics')

    def __str__(self):
        return f'{self.user.username}'

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        img = Image.open(self.image.path)
        if img.height > 300 or img.weidht > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.image.path)



class ClientUser(models.Model):
    user = models.OneToOneField(BaseUser, on_delete=models.CASCADE, related_name = 'client', primary_key=True)
    is_client = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.user.username} Client'

class ProfessionalUser(models.Model):
    user = models.OneToOneField(BaseUser, on_delete=models.CASCADE, related_name = 'professional', primary_key=True)
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


class ClientProfile(models.Model):
    client_profile = models.OneToOneField(ClientUser, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.user.username} Client Profile'



class ProfessionalProfile(models.Model):
    professional_profile = models.OneToOneField(ProfessionalUser, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.user.username} Professional Profile'