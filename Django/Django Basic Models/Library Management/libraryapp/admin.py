from django.contrib import admin
from .models import Book


# Register your models here.

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ["name","author","description","price","pages_count","sold_count","is_featured","is_trending","timestamp"]