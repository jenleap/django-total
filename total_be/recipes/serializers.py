from rest_framework import serializers

from foods.serializers import FoodSerializer
from .models import Recipe, Ingredient

class IngredientSerializer(serializers.ModelSerializer):
    food = FoodSerializer(many=False)
    
    class Meta:
        model = Ingredient
        fields = '__all__'

class RecipeFullSerializer(serializers.ModelSerializer):
    ingredients = IngredientSerializer(many=True)
    
    class Meta:
        model = Recipe
        fields = '__all__'

class RecipePartialSerializer(serializers.ModelSerializer):
    class Meta:
        model = Recipe
        fields = ("name")