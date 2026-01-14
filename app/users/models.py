from django.db import models

# Create your models here.
class User(models.Model):
    class Role(models.TextChoices):
        CUSTOMER = 'CUSTOMER', 'Customer'
        LANDLORD = 'LANDLORD', 'Landlord'

    
    username = models.CharField(max_length=150, unique=True)
    email = models.EmailField(unique=True, null=False, blank=False)
    first_name = models.CharField(max_length=30, blank=False, null=False)
    last_name = models.CharField(max_length=30, blank=False, null=False)
    
    rate = models.FloatField(default=10.0)    
    role = models.CharField(
        max_length=10,
        choices=Role.choices,
        blank=True,
        null=True,
    )    



