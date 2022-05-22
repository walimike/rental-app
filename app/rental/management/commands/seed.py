import random
import logging
import datetime
import pytz

from django.core.management.base import BaseCommand

from ...models import Rental, Reservations

logger = logging.getLogger(__name__)


# python manage.py seed --mode=refresh

""" Clear all data and creates reservations """
MODE_REFRESH = 'refresh'

""" Clear all data and do not create any object """
MODE_CLEAR = 'clear'

class Command(BaseCommand):
    help = "seed database for testing and development."

    def add_arguments(self, parser):
        parser.add_argument('--mode', type=str, help="Mode")

    def handle(self, *args, **options):
        self.stdout.write('seeding data...')
        run_seed(self, options['mode'])
        self.stdout.write('done.')

def generate_random_datetime():
    start_date = datetime.datetime(2022, 6, 1, 20, 8, 7, 127325, tzinfo=pytz.UTC)
    end_date = datetime.datetime(2022, 8, 1, 20, 8, 7, 127325, tzinfo=pytz.UTC)

    time_between_dates = end_date - start_date
    days_between_dates = time_between_dates.days
    random_number_of_days = random.randrange(days_between_dates)
    random_date = start_date + datetime.timedelta(days=random_number_of_days)
    return random_date

def clear_data():
    """Deletes all the table data"""
    logger.info("Delete Rental and Reservation instances")
    Rental.objects.all().delete()

def create_rentals():
    logger.info("Creating rentals")
    rental_names = [
        "Rentomatic",
        "Property",
        "Rental Network",
        "Solid Rental Property",
        "Dynamic Rentals",
        "Purple Properties"
    ]
    rentals = [Rental(name=name) for name in rental_names]
    Rental.objects.bulk_create(rentals)    


def create_reservations():
    """Creates an reseervation objects"""
    logger.info("Creating reservations")
    date = generate_random_datetime()
    rental = Rental.objects.order_by('?')[0]
    reservation = Reservations.objects.create(rental=rental, checkout=date)
    logger.info("{} created.".format(reservation))
    return reservation

def run_seed(self, mode):
    """ Seed database based on mode

    :param mode: refresh / clear 
    :return:
    """
    # Clear data from tables
    clear_data()
    if mode == MODE_CLEAR:
        return

    # Creating 20 reservations
    create_rentals()
    for i in range(20):
        create_reservations()