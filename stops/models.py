from django.db import models

# Create your models here.

from django.contrib.gis.db import models

class Stop(models.Model):
    name = models.CharField(max_length=100)
    location = models.PointField()
    category = models.CharField(max_length=50)
    address = models.CharField(max_length=100)
    city = models.CharField(max_length=50)
    desc = models.CharField(max_length=50)