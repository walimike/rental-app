from django.db import models

# Create your models here.

class Rental(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Reservations(models.Model):
    rental = models.ForeignKey(Rental, related_name='reservations', on_delete=models.CASCADE)
    checkin = models.DateTimeField(auto_now_add=True)
    checkout = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return f'{self.rental.name} reservation on {self.checkin}'

    @property
    def rental_name(self):
        return self.rental.name

    @property
    def previous_id(self):
        previous_item = self.rental.reservations.filter(id__lt=self.id)
        return previous_item.latest('id').id if previous_item.exists() else '----'
    
    @property
    def checkin_display(self):
        return self.checkin.date()

    @property
    def checkout_display(self):
        return self.checkout.date()
