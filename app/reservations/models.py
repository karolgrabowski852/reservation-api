import uuid
from django.db import models
from django.db.models import Avg
from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from app.users.models import User

# Create your models here.
class Accommodation(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=255)
    location = models.CharField(max_length=255)
    description = models.TextField()
    landlord = models.ForeignKey('users.User', on_delete=models.CASCADE)
    rating = models.FloatField(default=0.0)


class Reservation(models.Model):
    class Status(models.TextChoices):
        PENDING = 'PENDING', 'Pending'
        CONFIRMED = 'CONFIRMED', 'Confirmed'
        CANCELLED = 'CANCELLED', 'Cancelled'
    
    user = models.ForeignKey('users.User', on_delete=models.CASCADE)
    accommodation = models.ForeignKey(Accommodation, on_delete=models.CASCADE, null=True, blank=True)
    reservation_date = models.DateTimeField()
    status = models.CharField(max_length=20, choices=Status.choices)


class Review(models.Model):
    accommodation = models.ForeignKey(Accommodation, on_delete=models.CASCADE)
    user = models.ForeignKey('users.User', on_delete=models.CASCADE)
    rating = models.IntegerField(default=10)
    comment = models.TextField()


@receiver(post_save, sender=Review)
@receiver(post_delete, sender=Review)
def update_accommodation_rating(sender, instance, **kwargs):
    accommodation = instance.accommodation
    avg_rating = Review.objects.filter(accommodation=accommodation).aggregate(Avg('rating'))['rating__avg']
    accommodation.rating = avg_rating if avg_rating is not None else 0.0
    accommodation.save(update_fields=['rating'])




