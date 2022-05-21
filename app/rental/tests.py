import datetime

from django.test import TestCase
from django.test import Client

from .models import Rental, Reservations

now = datetime.datetime.now()
client = Client()
class ReservationsTestCase(TestCase):
    def setUp(self):
        for x in range(1,5):
            r = Rental.objects.create(name=f'Rental-{x}')
            Reservations.objects.bulk_create([
                Reservations(rental=r),
                Reservations(rental=r, checkout=now)
            ])

    def test_rentals_created(self):
        """Test rentals have been created in setup"""
        rentals = Rental.objects.all()
        self.assertEqual(rentals.count(), 4)

    def test_reservations_created(self):
        """Test reservations have been created in setup"""
        reservations = Reservations.objects.all()
        self.assertEqual(reservations.count(), 8)

    def test_ui_response(self):
        """Test index.html response"""
        response = client.get('/rental/')
        self.assertIn(b'Reservations table', response.content)
        self.assertIn(b'Rental_name', response.content)
        self.assertIn(b'Rental-3', response.content)
        self.assertEqual(response.context['reservations'].count(), 8)
