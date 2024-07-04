from django import forms
from django.contrib import admin
from django.utils.html import format_html

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

class RecipeForm(forms.ModelForm):
    class Meta:
        model = Recipe
        fields = '__all__'

class RecipeAdmin(admin.ModelAdmin):
    form = RecipeForm
    list_display = ['name', 'description', 'serving_size', 'recipe_yield', 'photo_preview']
    readonly_fields = ['photo_preview']
    inlines = [IngredientInline, StepInline]

    def photo_preview(self, obj):
        if obj.photo:
            return format_html('<img src="{}" width="100" height="100" />', obj.photo.url)
        return "(No photo)"
    photo_preview.allow_tags = True
    photo_preview.short_description = 'Photo Preview'

class CategoryAdmin(admin.ModelAdmin):
    search_fields = ['label']

admin.site.register(Recipe, RecipeAdmin)
admin.site.register(Category, CategoryAdmin)