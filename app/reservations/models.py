import uuid
from django.db import models
from app.users.models import User

# Create your models here.
class Accommodation(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=255)
    location = models.CharField(max_length=255)
    description = models.TextField()
    landlord = models.ForeignKey('users.User', on_delete=models.CASCADE)
    reservations = models.ForeignKey('Reservation', on_delete=models.CASCADE, null=True, blank=True)
    rating = models.FloatField(default=10.0)


class Reservation(models.Model):
    class Status(models.TextChoices):
        PENDING = 'PENDING', 'Pending'
        CONFIRMED = 'CONFIRMED', 'Confirmed'
        CANCELLED = 'CANCELLED', 'Cancelled'
    
    user = models.ForeignKey('users.User', on_delete=models.CASCADE)
    reservation_date = models.DateTimeField()
    status = models.CharField(max_length=20, choices=Status.choices)


class Review(models.Model):
    accommodation = models.ForeignKey(Accommodation, on_delete=models.CASCADE)
    user = models.ForeignKey('users.User', on_delete=models.CASCADE)
    rating = models.IntegerField(default=10)
    comment = models.TextField()


