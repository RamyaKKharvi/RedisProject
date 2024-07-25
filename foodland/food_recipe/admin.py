from django.contrib import admin
from .models import Recipe


@admin.register(Recipe)
class RecipeAdmin(admin.ModelAdmin):
    fields = ['name', 'intro', 'ingredients', 'directions', 'tip', 'image']
