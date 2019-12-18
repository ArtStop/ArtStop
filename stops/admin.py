from django.contrib.gis.admin import OSMGeoAdmin
from .models import Stop

@admin.register(Stop)
class StopAdmin(OSMGeoAdmin):
    list_display = ('name', 'location')