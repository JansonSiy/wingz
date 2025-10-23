from django.db import models

class User(models.Model):
    ROLE_CHOICES = [
        ('admin', 'Admin'),
        ('rider', 'Rider'),
        ('driver', 'Driver'),
    ]

    role = models.CharField(max_length=255, choices=ROLE_CHOICES)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.EmailField(max_length=255, unique=True)
    phone_number = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return f'{self.first_name} {self.last_name} ({self.role})'


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

    def __str__(self):
        return f'Driver: {self.id_driver.first_name} {self.id_driver.last_name} | Rider: {self.id_rider.first_name} {self.id_rider.last_name} | Status: {self.status}'

class RideEvent(models.Model):
    ride = models.ForeignKey('Ride', on_delete=models.CASCADE)
    description = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.ride} | {self.description[:20]}...'