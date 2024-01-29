from django.db import models


class Products(models.Model):
    name = models.CharField(
        verbose_name="Название продукта", unique=True, max_length=25
    )
    num_of_product_preparations = models.IntegerField(
        verbose_name="Сколько раз продукт использовался в приготовлении", default=0
    )

    class Meta:
        verbose_name = "Продукт"
        verbose_name_plural = "Продукты"

    def __str__(self):
        return self.name
