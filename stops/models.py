from django.db import models
import django.utils.timezone as timezone

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
    desc = models.CharField(max_length=50) 

class RatingModel(models.Model):
    bar = models.CharField(max_length=100)
    ratings = GenericRelation(Rating, related_query_name='ratings')

class Comment(models.Model):
    stop = models.ForeignKey(Stop, on_delete=models.CASCADE, related_name='comments')
    author = models.CharField(max_length=200, default="guest")
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    approved_comment = models.BooleanField(default=False)

    def approve(self):
        self.approved_comment = True
        self.save()

    def __str__(self):
        return self.text
