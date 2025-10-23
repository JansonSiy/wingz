from django.db import models

class User(models.Model):
    ROLE_CHOICES = [
        ('rider', 'Rider'),
        ('driver', 'Driver'),
    ]

    role = models.CharField(max_length=255, choices=ROLE_CHOICES)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.EmailField(max_length=255)
    phone_number = models.CharField(max_length=255)

class Ride(models.Model):
    STATUS_CHOICES = [
        ('en-route', 'En Route'),
        ('pickup', 'Pickup'),
        ('dropoff', 'Dropoff'),
    ]

    status = models.CharField(max_length=255, choices=STATUS_CHOICES, default='pickup')
    id_rider = models.ForeignKey('User', on_delete=models.CASCADE, related_name='rider')
    id_driver = models.ForeignKey('User', on_delete=models.CASCADE, related_name='driver')
    pickup_latitude = models.FloatField()
    pickup_longitude = models.FloatField()
    dropoff_latitude = models.FloatField()
    dropoff_longitude = models.FloatField()
    pickup_time = models.DateTimeField()

class RideEvent(models.Model):
    ride = models.ForeignKey('Ride', on_delete=models.CASCADE)
    description = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
