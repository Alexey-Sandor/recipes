from django.db import models
from django.db.models import Q


class RecipesManager(models.Manager):
    def without_product(self, product):
        return self.filter(
            ~Q(ingredients__product=product)
            | (Q(ingredients__product=product) & Q(ingredients__weight_in_grams__lt=10))
        ).distinct()


class Recipes(models.Model):
    objects = RecipesManager()
    name = models.CharField(max_length=30, verbose_name="Название рецепта")
    ingredient = models.ManyToManyField(
        "Products", verbose_name="Ингредиент", through="Ingredients"
    )

    class Meta:
        verbose_name = "Рецепт"
        verbose_name_plural = "Рецепты"

    def __str__(self):
        return self.name
