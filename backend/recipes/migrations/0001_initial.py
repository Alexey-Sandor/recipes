# Generated by Django 3.0 on 2024-01-29 17:20

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Ingredients",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("weight_in_grams", models.IntegerField(verbose_name="Вес в граммах")),
            ],
            options={
                "verbose_name": "Ингредиент",
                "verbose_name_plural": "Ингредиенты",
            },
        ),
        migrations.CreateModel(
            name="Products",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "name",
                    models.CharField(
                        max_length=25, unique=True, verbose_name="Название продукта"
                    ),
                ),
                (
                    "num_of_product_preparations",
                    models.IntegerField(
                        default=0,
                        verbose_name="Сколько раз продукт использовался в приготовлении",
                    ),
                ),
            ],
            options={
                "verbose_name": "Продукт",
                "verbose_name_plural": "Продукты",
            },
        ),
        migrations.CreateModel(
            name="Recipes",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "name",
                    models.CharField(max_length=30, verbose_name="Название рецепта"),
                ),
                (
                    "ingredient",
                    models.ManyToManyField(
                        through="recipes.Ingredients",
                        to="recipes.Products",
                        verbose_name="Ингредиент",
                    ),
                ),
            ],
            options={
                "verbose_name": "Рецепт",
                "verbose_name_plural": "Рецепты",
            },
        ),
        migrations.AddField(
            model_name="ingredients",
            name="product",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                to="recipes.Products",
                verbose_name="Продукт",
            ),
        ),
        migrations.AddField(
            model_name="ingredients",
            name="recipe",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                to="recipes.Recipes",
                verbose_name="Рецепт",
            ),
        ),
        migrations.AlterUniqueTogether(
            name="ingredients",
            unique_together={("product", "recipe")},
        ),
    ]
