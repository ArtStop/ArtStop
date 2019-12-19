from django.shortcuts import render

# views here.
from django.views import generic
from django.contrib.gis.geos import fromstr
from django.contrib.gis.db.models.functions import Distance
from .models import Stop
from django.contrib.gis.geos import Point
import json, requests
info = requests.get('http://ipinfo.io/json').json()
result = [x.strip() for x in info['loc'].split(',')]
latitude, longitude = result

user_location = Point(float(longitude), float(latitude), srid=4326)

class Home(generic.ListView):
    model = Stop
    context_object_name = 'stops'
    queryset = Stop.objects.annotate(distance=Distance('location',
    user_location)
    ).order_by('distance')[0:6]
    template_name = 'stops/index.html'