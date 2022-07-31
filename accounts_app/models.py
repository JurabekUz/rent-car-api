from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy

from accounts_app.manager import CustomUserManager

class CustomUser(AbstractUser):
    phone = models.CharField(max_length=20, blank=True, null=True)
    age = models.PositiveSmallIntegerField(blank=True, null=True)
    address = models.CharField(max_length=100, blank=True, null=True)
    email = models.EmailField(
        gettext_lazy('email address'),  # verbose_name ishlatsak ham boladi
        max_length=100,
        unique=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['phone', 'age', 'address']

    objects = CustomUserManager()

    def __str__(self):
        return self.email
