from django.db import models

# Create your models here.

class Food(models.Model):
    name = models.CharField(max_length=200, null=False)
    brand = models.CharField(max_length=200, null=True, blank=True)

    def __str__(self):
        return self.name

class Measure(models.Model):
    UNITS_OF_MEASURE = {
        "0": "custom",
        "1": "g",
        "2": "oz",
        "3": "lb(s)",
        "4": "cup(s)",
        "5": "tbsp",
        "6": "tsp",
        "7": "serving(s)"
    }
    food = models.ForeignKey(Food, related_name='measures', on_delete=models.CASCADE, null=False)
    quantity = models.DecimalField(max_digits=6, decimal_places=2, null=False)
    unit = models.CharField(max_length=1, choices=UNITS_OF_MEASURE)
    custom_unit = models.CharField(max_length=100, null=True, blank=True)
    calories = models.DecimalField(max_digits=6, decimal_places=2, null=False)
    carbs = models.DecimalField(max_digits=6, decimal_places=2)
    protein = models.DecimalField(max_digits=6, decimal_places=2)
    fat = models.DecimalField(max_digits=6, decimal_places=2)
    fiber = models.DecimalField(max_digits=6, decimal_places=2, null=True, blank=True)


