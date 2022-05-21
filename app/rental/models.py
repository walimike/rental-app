from django.db import models

# Create your models here.

class Rental(models.Model):
    name = models.CharField(max_length=200)


class Reservation(models.Model):
    rental = models.ForeignKey(Rental, related_name='reservations', on_delete=models.CASCADE)
    checkin = models.DateTimeField(auto_now_add=True)
    checkout = models.DateTimeField(null=True, blank=True)
