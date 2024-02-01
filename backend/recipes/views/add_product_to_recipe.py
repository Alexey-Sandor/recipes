from django.http import HttpResponse
from django.shortcuts import get_object_or_404

from ..models import Ingredients, Products, Recipes


def add_product_to_recipe(request, recipe_id, product_id, weight):
    recipe = get_object_or_404(Recipes, pk=recipe_id)
    product = get_object_or_404(Products, pk=product_id)

    ingredient, created = Ingredients.objects.get_or_create(
        recipe=recipe, product=product, defaults={"weight_in_grams": weight}
    )

    if not created:
        ingredient.weight_in_grams = weight
        ingredient.save()

    return HttpResponse("Продукт добавлен в рецепт")
