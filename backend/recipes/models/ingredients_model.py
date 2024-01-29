from django.db import models


class Ingredients(models.Model):
    product = models.ForeignKey(
        "Products", on_delete=models.CASCADE, verbose_name="Продукт"
    )
    recipe = models.ForeignKey(
        "Recipes", on_delete=models.CASCADE, verbose_name="Рецепт"
    )
    weight_in_grams = models.IntegerField(verbose_name="Вес в граммах")

    def __str__(self):
        return self.product.name

    class Meta:
        verbose_name = "Ингредиент"
        verbose_name_plural = "Ингредиенты"
        unique_together = ("product", "recipe")
