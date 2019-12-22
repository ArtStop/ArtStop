from django.shortcuts import render

# views here.
from django.views import generic
from django.contrib.gis.geos import fromstr
from django.contrib.gis.db.models.functions import Distance
from .models import Stop
from .filters import StopFilter
from django.contrib.gis.geos import Point
import json, requests
info = requests.get('http://ipinfo.io/json').json()
result = [x.strip() for x in info['loc'].split(',')]
latitude, longitude = result

user_location = Point(float(longitude), float(latitude), srid=4326)

class Home(generic.ListView):
    model = Stop
    context_object_name = 'stops'
    qs_names = [stop.name for stop in Stop.objects.annotate(distance=Distance('location',
    user_location)
    ).order_by('distance')[:10]]
    queryset = Stop.objects.all().filter(name__in=qs_names)

    template_name = 'stops/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filter'] = StopFilter(self.request.GET, queryset=self.get_queryset())
        return context

class StopDetailView(generic.DetailView):
    model = Stop
