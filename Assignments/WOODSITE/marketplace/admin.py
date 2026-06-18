from django.contrib import admin
from .models import *

# Register your models here.
@admin.register(Role)
class RoleAdmin(admin.ModelAdmin):
    list_display = ('user_typename',)

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('u_name','user_image','u_gender','u_email','u_phone','u_type','u_status')

@admin.register(FurnitureCategory)
class FurnitureCategoryAdmin(admin.ModelAdmin):
    list_display = ('cat_name','furniture_image','cat_desc','category_added')

@admin.register(Country)
class CountryAdmin(admin.ModelAdmin):
    list_display = ('country_name',)

@admin.register(State)
class StateAdmin(admin.ModelAdmin):
    list_display = ('country_id','state_name')

@admin.register(City)
class CityAdmin(admin.ModelAdmin):
    list_display = ('state_id','city_name')

@admin.register(UserAddress)
class UserAddressAdmin(admin.ModelAdmin):
    list_display = ('user_address','building_name','street_name','city_name','pin_code')

@admin.register(FeedBackDetails)
class FeedBackDetailsAdmin(admin.ModelAdmin):
    list_display = ('f_title','f_description','f_by','f_on')

@admin.register(ComplaintDetails)
class ComplaintDetailsAdmin(admin.ModelAdmin):
    list_display = ('c_name','c_detail','complaint_photo','c_by','c_on')

@admin.register(Brand)
class BrandAdmin(admin.ModelAdmin):
    list_display = ('brand_name','brand_description','brand_image')

@admin.register(NewFurniture)
class NewFurnitureAdmin(admin.ModelAdmin):
    list_display = ('f_name','brand_name','furniture_description','furniture_price','furniture_photo','furniture_type','available_quantity')

@admin.register(OldFurniture)
class OldFurnitureAdmin(admin.ModelAdmin):
    list_display = ('old_furniture_name','old_furniture_brand_name','old_furniture_description','old_furniture_price','old_furniture_photo','old_furniture_type','available_quantity')

@admin.register(RentFurniture)
class RentFurnitureAdmin(admin.ModelAdmin):
    list_display = ('rent_furniture_name','rent_brand_name','rent_furniture_description','rent_furniture_price','rent_furniture_photo','rent_furniture_type','available_quantity')

@admin.register(NewFurnitureBuying)
class NewFurnitureBuyingAdmin(admin.ModelAdmin):
    list_display = ('furniture','user','booking_datetime')

@admin.register(OldFurnitureBuying)
class OldFurnitureAdmin(admin.ModelAdmin):
    list_display = ('old_furniture','user_booking','old_booking_datetime')

@admin.register(RentFurnitureOrder)
class RentFurnitureOrderAdmin(admin.ModelAdmin):
    list_display = ('rent_furniture','rent_userid','rent_start_date','rent_end_date','rent_book_datetime')