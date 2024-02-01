from django.db import transaction
from django.http import HttpResponse

from ..models import Ingredients, Products


@transaction.atomic
def cook_recipe(request, recipe_id):
    ingredients = Ingredients.objects.filter(recipe_id=recipe_id)

    for ingredient in ingredients:
        ingredient.product.num_of_product_preparations += 1

    Products.objects.bulk_update(
        [ingredient.product for ingredient in ingredients],
        ["num_of_product_preparations"],
    )

    return HttpResponse(
        "Количество приготовлений с использованием продуктов рецепта увеличено на 1"
    )
