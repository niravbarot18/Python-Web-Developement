from django.contrib import admin
from .models import *
# Register your models here.

@admin.register(Country)
class CountryAdmin(admin.ModelAdmin):
    list_display= ("country_name",)

@admin.register(State)
class StateAdmin(admin.ModelAdmin):
    list_display=("country","state_name")

@admin.register(City)
class CityAdmin(admin.ModelAdmin):
    list_display=("state","city_name")

@admin.register(Actor)
class ActorAdmin(admin.ModelAdmin):
    list_display = ("a_state","a_country","a_city","a_name","a_profile","a_bio","a_nationality","a_awards","a_gender","a_birthdate")

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ("u_state","u_country","u_city","u_name","u_gender","u_email","u_phone","u_status","u_date_joined")

@admin.register(Director)
class DirectorAdmin(admin.ModelAdmin):
    list_display = ("d_state","d_country","d_city","d_name","d_bio","d_nationality","d_awards","d_gender")

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("name",)

@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    list_display = ("title","description","release_year","category","get_actors","director","trailer","created_at")

@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ("movie","user","rating","comment","created_at")

@admin.register(Watchlist)
class WatchlistAdmin(admin.ModelAdmin):
    list_display = ("user","movie","added_at")