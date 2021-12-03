from django.db import models
from django.contrib.auth.models import AbstractUser
from .managers import CustomUserManager
from django.utils.translation import ugettext_lazy as _

# Create your models here.

class Users(AbstractUser):
    MaDG = models.AutoField(primary_key=True)
    username = models.CharField(max_length=100, blank=True)
    email = models.EmailField(_('email address'), unique=True)
    birth_date = models.DateField(blank=True, null=True)
    phone_number = models.CharField(max_length=20, null=True, blank=True)
    ngaylapthe = models.DateField(null=True, blank=True)
    ngayhethan = models.DateField(null=True, blank=True)
    is_reader = models.BooleanField(default=True)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    objects = CustomUserManager()

    def __str__(self):
        return self.email