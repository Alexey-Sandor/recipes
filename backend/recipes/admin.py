from django.contrib import admin
from .models import Products, Recipes, Ingredients


class IngredientInline(admin.TabularInline):
    model = Ingredients


class RecipeAdmin(admin.ModelAdmin):
    inlines = [IngredientInline]


admin.site.register(Products)
admin.site.register(Recipes, RecipeAdmin)
