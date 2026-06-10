from django.contrib import admin
from .models import *

# Register your models here.

@admin.register(BookCategory)
class BookCategoryAdmin(admin.ModelAdmin):
    list_display = ["category_name","category_description"]

@admin.register(BookAuthor)
class BookAuthorAdmin(admin.ModelAdmin):
    list_display = ["author_name","author_bio"]

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ["title","category_id","author_id","pages","publisher","publication_year","isbn"]

