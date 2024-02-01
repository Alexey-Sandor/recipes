from django.db import transaction
from django.http import HttpResponse

from ..models import Ingredients


@transaction.atomic
def cook_recipe(request, recipe_id):
    ingredients = Ingredients.objects.filter(recipe_id=recipe_id)

    for ingredient in ingredients:
        ingredient.num_of_product_preparations += 1

    Ingredients.objects.bulk_update(ingredients, ["num_of_product_preparations"])

    return HttpResponse(
        "Количество приготовлений с использованием продуктов рецепта увеличено на 1"
    )
