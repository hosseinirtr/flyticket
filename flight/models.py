from django.db import models
from django.core.exceptions import ValidationError
from accounts.models import User


class Airport(models.Model):
    city = models.CharField(max_length=50, unique=True)
    code = models.CharField(max_length=10, unique=True)

    def __str__(self):
        return f"{self.code} airport is at {self.city} "


class Flight(models.Model):
    origin = models.ForeignKey(Airport, on_delete=models.CASCADE, related_name="origin")
    destination = models.ForeignKey(Airport, on_delete=models.CASCADE, related_name="destination")
    capacity = models.IntegerField(null=False)
    date = models.DateField(null=False)

    def clean(self):
        if self.destination == self.origin:
            raise ValidationError("Origin and destination can't be the same")

    def save(self, *args, **kwargs):
        self.clean()
        super(Flight, self).save(*args, **kwargs)

    def __str__(self):
        return f"{self.origin} - {self.destination} , date: {self.date}, capacity: {self.capacity} "


class Passenger(models.Model):
    flight = models.ForeignKey(Flight, on_delete=models.CASCADE)
    account = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.flight} - {self.account.username}"
