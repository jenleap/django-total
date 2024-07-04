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
    categories = models.ManyToManyField(Category, related_name='recipes')
    photo = models.ImageField(upload_to='recipe_photos/', null=True, blank=True)

    def __str__(self):
        return self.name
    
    def macros(self):
        
        total_calories = sum([ingredient.macros()["calories"] for ingredient in self.ingredients.all()])
        total_carbs = sum([ingredient.macros()["carbs"] for ingredient in self.ingredients.all()])
        total_protein = sum([ingredient.macros()["protein"] for ingredient in self.ingredients.all()])
        total_fat = sum([ingredient.macros()["fat"] for ingredient in self.ingredients.all()])
        total_fiber = sum([ingredient.macros()["fiber"] for ingredient in self.ingredients.all()])

        return {
            "calories": total_calories / self.recipe_yield,
            "carbs": total_carbs / self.recipe_yield,
            "protein": total_protein / self.recipe_yield,
            "fat": total_fat / self.recipe_yield,
            "fiber": total_fiber / self.recipe_yield
        }

class Ingredient(models.Model):
    food = models.ForeignKey(Food, on_delete=models.CASCADE, null=False)
    recipe = models.ForeignKey(Recipe, related_name='ingredients', on_delete=models.CASCADE, null=False)
    quantity = models.DecimalField(max_digits=6, decimal_places=2, null=False)
    unit = models.CharField(max_length=1, choices=Measure.UNITS_OF_MEASURE)
    notes = models.CharField(max_length=200, null=True, blank=True)

    def get_measure(self):
        return self.food.get_measure_by_unit(self.unit)

    def name(self):
        measure = self.get_measure()
        simple_name = f"{self.quantity} {measure.unit_label()} {self.food.name}"
        if self.notes:
            return f"{simple_name}, {self.notes}"
        return simple_name

    def macros(self):
        measure = self.get_measure()
        multiplier = self.quantity / measure.quantity
        return {
            "calories": multiplier * measure.calories,
            "carbs": multiplier * measure.carbs,
            "protein": multiplier * measure.protein,
            "fat": multiplier * measure.fat,
            "fiber": multiplier * measure.fiber
        }
               

class Step(models.Model):
    recipe = models.ForeignKey(Recipe, related_name='steps', on_delete=models.CASCADE, null=False)
    order = models.IntegerField()
    instruction = models.TextField()
