from django.db import models

# Create your models here.

from django.contrib.gis.db import models
from django.contrib.contenttypes.fields import GenericRelation
from star_ratings.models import Rating

class Stop(models.Model):
    name = models.CharField(max_length=100)
    location = models.PointField()
    category = models.CharField(max_length=50)
    address = models.CharField(max_length=100)
    city = models.CharField(max_length=50)

class RatingModel(models.Model):
    bar = models.CharField(max_length=100)
    ratings = GenericRelation(Rating, related_query_name='ratings')
