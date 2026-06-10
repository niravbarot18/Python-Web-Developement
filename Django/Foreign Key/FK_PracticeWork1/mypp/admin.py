from django.contrib import admin
from .models import *

# Register your models here.

@admin.register(PlayerCategory)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("category_name","category_description")

@admin.register(PlayerTeam)
class TeamAdmin(admin.ModelAdmin):
    list_display = ("team_name","team_description")

@admin.register(Player)
class PlayerAdmin(admin.ModelAdmin):
    list_display = ("name","category_id","team_id","runs","wickets","hundreds","fifties","jersey_no")