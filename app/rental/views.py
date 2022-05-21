from django.template import loader

from django.http import HttpResponse
from .models import Reservations


def index(request):
  reservations = Reservations.objects.all()
  template = loader.get_template('rental/index.html')
  context = {
    'reservations': reservations,
  }
  return HttpResponse(template.render(context, request))