from django import forms
from django.contrib import admin

from .models import Category, Ingredient, Recipe, Step

# Register your models here.

class IngredientForm(forms.ModelForm):
    class Meta:
        model = Ingredient
        fields = '__all__'

    def clean(self):
        cleaned_data = super().clean()
        food = cleaned_data.get('food')
        unit = cleaned_data.get('unit')

        if food and unit:
            measure_units = [measure.unit for measure in food.measures.all()]
            if unit not in measure_units:
                raise forms.ValidationError(f"The unit '{unit}' is not valid for the selected food. Allowed units: {', '.join(measure_units)}")
        
        return cleaned_data

class IngredientInline(admin.StackedInline):
    model = Ingredient
    extra = 1
    autocomplete_fields = ['food']

class StepInline(admin.StackedInline):
    model = Step
    extra = 1

class RecipeAdmin(admin.ModelAdmin):
    inlines = [IngredientInline, StepInline]

class CategoryAdmin(admin.ModelAdmin):
    search_fields = ['label']

admin.site.register(Recipe, RecipeAdmin)
admin.site.register(Category, CategoryAdmin)