from django.contrib import admin
from .models import *

# Register your models here.

@admin.register(Role)
class RoleAdmin(admin.ModelAdmin):
    list_display = ("user_typename",)

@admin.register(UserDetails)
class UserDetailsAdmin(admin.ModelAdmin):
    list_display = ("u_name","user_image","u_gender","u_email","u_phone","u_type","u_status")

@admin.register(CarCategory)
class CarCategoryAdmin(admin.ModelAdmin):
    list_display = ("cat_name","cat_picture","cat_description","category_added")

@admin.register(Country)
class CountryAdmin(admin.ModelAdmin):
    list_display = ("country_name",)

@admin.register(State)
class StateAdmin(admin.ModelAdmin):
    list_display = ("country_id","state_name")

@admin.register(City)
class CityAdmin(admin.ModelAdmin):
    list_display = ("state_id","city_name")

@admin.register(UserAddress)
class UserAddressAdmin(admin.ModelAdmin):
    list_display = ("u_id","building_name","street_name","city_name","pin_code")

@admin.register(FeedbackDetails)
class FeedbackDetailsAdmin(admin.ModelAdmin):
    list_display = ("f_title","f_description","f_by","f_on")

@admin.register(ComplaintDetails)
class ComplaintDetailsAdmin(admin.ModelAdmin):
    list_display = ("c_name","c_detail","complaint_photo","c_by","c_on")
