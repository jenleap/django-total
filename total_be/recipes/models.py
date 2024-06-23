from django.db import models

from foods.models import Food, Measure

# Create your models here.

class Category(models.Model):
    label = models.CharField(max_length=100)

    def __str__(self):
        return self.label

class Recipe(models.Model):
    name = models.CharField(max_length=200, null=False)
    description = models.TextField()
    recipe_yield = models.IntegerField()
    serving_size = models.CharField(max_length=100)
    categories = models.ManyToManyField(Category)

    def __str__(self):
        return self.name

class Ingredient(models.Model):
    food = models.ForeignKey(Food, on_delete=models.CASCADE, null=False)
    recipe = models.ForeignKey(Recipe, related_name='ingredients', on_delete=models.CASCADE, null=False)
    quantity = models.DecimalField(max_digits=6, decimal_places=2, null=False)
    unit = models.CharField(max_length=1, choices=Measure.UNITS_OF_MEASURE)
    notes = models.CharField(max_length=200, null=True, blank=True)

class Step(models.Model):
    recipe = models.ForeignKey(Recipe, related_name='steps', on_delete=models.CASCADE, null=False)
    order = models.IntegerField()
    instruction = models.TextField()
