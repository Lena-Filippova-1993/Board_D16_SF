from django.db import models
from django.contrib.auth.models import AbstractUser


class AuthUser(models.Model):
    pass
# Create your models here.
# class User(AbstractUser):
#     code = models.CharField(max_length=25, blank=True, null=True)


class OneTimeCode(models.Model):
    user = models.CharField(max_length=256)
    code = models.CharField(max_length=10)
