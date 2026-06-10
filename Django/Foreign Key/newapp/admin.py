from django.contrib import admin
from .models import *

# Register your models here.
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("name","description")

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ("category_id","product_name","product_description","product_price","product_quantity")
