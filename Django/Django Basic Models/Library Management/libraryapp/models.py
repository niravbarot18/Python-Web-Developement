from django.db import models

# Create your models here.

class Book(models.Model):
    name = models.CharField(max_length=20)
    author = models.CharField(max_length=20)
    description = models.TextField()
    price = models.FloatField()
    pages_count = models.IntegerField()
    sold_count = models.IntegerField()
    is_featured = models.BooleanField()
    is_trending = models.BooleanField()
    timestamp = models.DateTimeField(auto_now_add=True)