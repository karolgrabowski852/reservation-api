from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.
class User(AbstractUser):
    class Role(models.TextChoices):
        CUSTOMER = 'CUSTOMER', 'Customer'
        LANDLORD = 'LANDLORD', 'Landlord'

    email = models.EmailField(unique=True, null=False, blank=False)
    role = models.CharField(
        max_length=10,
        choices=Role.choices,
        blank=True,
        null=True,
    )    



