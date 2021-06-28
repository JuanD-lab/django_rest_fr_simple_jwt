from typing import AbstractSet
from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class UserCustom(AbstractUser):
    edad = models.IntegerField(null=True)