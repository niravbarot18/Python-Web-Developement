from django.db import models

# Create your models here.
class Category(models.Model):
    category_name = models.CharField(max_length=20)
    description = models.TextField()

    def __str__(self):
        return self.name

class Product(models.Model):
    category_id = models.ForeignKey(Category, on_delete=models.CASCADE)
    product_name = models.CharField(max_length=20)
    product_description = models.TextField()
    product_price = models.FloatField()
    product_quantity = models.IntegerField()