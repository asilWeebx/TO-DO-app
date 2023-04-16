
from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.


class User(AbstractUser):
    is_active = models.BooleanField(default=True)
    profile_image = models.FileField(upload_to='images/')