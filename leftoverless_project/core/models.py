from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
class Profile(models.Model):
    ROLE_CHOICES = (
        ('donor', 'Donor'),
        ('receiver', 'Receiver'),
        ('volunteer', 'Volunteer'),
    )

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    role = models.CharField(max_length=20, choices=ROLE_CHOICES)
    full_name = models.CharField(max_length=100, default="User")

    def __str__(self):
        return f"{self.full_name} ({self.role})"


from django.db import models
from django.contrib.auth.models import User


class Food(models.Model):

    STATUS_CHOICES = [
        ('available', 'Available'),
        ('requested', 'Requested'),
        ('assigned', 'Assigned to Volunteer'),
        ('picked', 'Picked Up'),
        ('delivered', 'Delivered'),
        ('cancelled', 'Cancelled'),
        ('expired', 'Expired'),
    ]

    donor = models.ForeignKey(User, on_delete=models.CASCADE)

    food_name = models.CharField(max_length=100)
    food_type = models.CharField(max_length=50)
    quantity = models.IntegerField()

    prepared_time = models.DateTimeField()
    expiry_time = models.DateTimeField()

    address = models.TextField()
    latitude = models.FloatField(null=True, blank=True)
    longitude = models.FloatField(null=True, blank=True)
    notes = models.TextField(blank=True)

    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default='available'
    )

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.food_name} ({self.status})"


latitude = models.DecimalField(max_digits=9, decimal_places=6, null=True, blank=True)
longitude = models.DecimalField(max_digits=9, decimal_places=6, null=True, blank=True)
