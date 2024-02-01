from django.urls import path

from .views import (add_product_to_recipe, cook_recipe,
                    show_recipes_without_product)

urlpatterns = [
    path(
        "add_product_to_recipe/<recipe_id>/<product_id>/<weight>",
        add_product_to_recipe,
        name="add_product",
    ),
    path("cook_recipe/<int:recipe_id>", cook_recipe, name="cook_recipe"),
    path(
        "show_recipes_without_product/<product_id>",
        show_recipes_without_product,
        name="show_recipes_without_product",
    ),
]
