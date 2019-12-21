from django.contrib import admin

# Register your models here.

from django.contrib.gis.admin import OSMGeoAdmin
from .models import Stop

@admin.register(Stop)
class StopAdmin(OSMGeoAdmin):
    list_display = ('name', 'category', 'location')