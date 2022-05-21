from django.contrib import admin

from .models import Rental, Reservations


class RentalAdmin(admin.ModelAdmin):
    fields = ['name']
    list_display = ('id', 'name')


class ReservationsAdmin(admin.ModelAdmin):
    fields = ['checkout', 'rental']
    list_display = ('id', 'checkin', 'checkout', 'rental')

admin.site.register(Rental, RentalAdmin)
admin.site.register(Reservations, ReservationsAdmin)
