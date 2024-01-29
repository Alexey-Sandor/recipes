from django.http import HttpResponse
from django.shortcuts import get_object_or_404

from ..models import Recipes


def cook_recipe(request, recipe_id):
    recipe = get_object_or_404(Recipes, id=recipe_id)
    for ingredient in recipe.ingredient.all():
        ingredient.num_of_product_preparations += 1
        ingredient.save()
    return HttpResponse(
        "Количество приготовлений с использованием продуктов рецепта увеличено на 1"
    )
