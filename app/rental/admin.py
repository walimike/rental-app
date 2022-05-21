from django.contrib import admin

from .models import Rental, Reservation


class RentalAdmin(admin.ModelAdmin):
    fields = ['name']
    list_display = ('id', 'name')


class ReservationAdmin(admin.ModelAdmin):
    fields = ['checkout', 'rental']
    list_display = ('id', 'checkin', 'checkout', 'rental')

admin.site.register(Rental, RentalAdmin)
admin.site.register(Reservation, ReservationAdmin)
