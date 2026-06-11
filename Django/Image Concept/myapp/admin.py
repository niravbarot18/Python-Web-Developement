from django.contrib import admin
from .models import *
# Register your models here.

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ("name","title","description","image_book","publish_date")

@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ("name","age","bio","author_image","total_books","famous_book","genre","city","state","country")