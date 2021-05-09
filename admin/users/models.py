from django.db import models
from django.core.validators import RegexValidator


class User(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(max_length=256)
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$', message="Invalid number!")
    mobile = models.CharField(validators=[phone_regex], max_length=17, blank=True)
    