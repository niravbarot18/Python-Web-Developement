from django.db import models

# Create your models here.
class BookCategory(models.Model):
    category_name = models.CharField(max_length=30)
    category_description = models.TextField()
    def __str__(self):
        return self.category_name

class BookAuthor(models.Model):
    author_name = models.CharField(max_length=30)
    author_bio = models.TextField()
    def __str__(self):
        return self.author_name

class Book(models.Model):
    title = models.CharField(max_length=50)
    category_id=models.ForeignKey(BookCategory, on_delete=models.CASCADE)
    author_id=models.ForeignKey(BookAuthor, on_delete=models.CASCADE)
    pages=models.IntegerField()
    publisher=models.CharField(max_length=50)
    publication_year=models.IntegerField()
    isbn=models.IntegerField()

    def __str__(self):
        return self.title

