from django.db import models
from django.utils.safestring import mark_safe

available_genre =[
    ('crime','Crime'),
    ('drama','Drama'),
    ('thriller','Thriller'),
    ('action','Action'),
    ('comedy','Comedy'),
    ('horror','Horror'),
]
# Create your models here.

class Book(models.Model):
    name=models.CharField(max_length=25)
    title=models.CharField(max_length=50)
    description=models.TextField()
    image=models.ImageField(upload_to="photos")
    publish_date=models.DateTimeField(auto_now_add=True,editable=False)

    def __str__(self):
        return self.name

    def image_book(self):
        return mark_safe("<img src='{}' width='100' />".format(self.image.url))

class Author(models.Model):
    name=models.CharField(max_length=25)
    age=models.IntegerField()
    bio=models.TextField()
    image=models.ImageField(upload_to="photos")
    total_books=models.IntegerField()
    famous_book=models.CharField(max_length=30)
    genre=models.CharField(max_length=25,choices=available_genre)
    city=models.CharField(max_length=25)
    state=models.CharField(max_length=25)
    country=models.CharField(max_length=25)

    def __str__(self):
        return self.name

    def author_image(self):
        return mark_safe("<img src='{}' width='100' />".format(self.image.url))
