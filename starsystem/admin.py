from django.contrib import admin
from .models import Planet, Star
# Register your models here.

@admin.register(Planet)
class PlanetAdmin(admin.ModelAdmin):
    list_display = ('name', 'has_atmosphere', 'has_water', 'star')

@admin.register(Star)
class StarAdmin(admin.ModelAdmin):
    list_display = ('name', 'star_type')