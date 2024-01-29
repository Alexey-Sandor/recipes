from django.shortcuts import render, get_object_or_404

from ..models import Recipes, Products


def show_recipes_without_product(request, product_id):
    product = get_object_or_404(Products, id=product_id)
    recipes = Recipes.objects.without_product(product)
    return render(request, "show_recipes_without_product.html", {"recipes": recipes})
