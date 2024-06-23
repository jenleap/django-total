from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import Recipe
from .serializers import RecipeFullSerializer, RecipePartialSerializer


@api_view(['GET'])
def getRecipes(request):
    recipes = Recipe.objects.all()
    serializedRecipes = RecipePartialSerializer(recipes, many=True)
    return Response(serializedRecipes.data)

@api_view(['GET'])
def getRecipe(request, id):
    recipe = Recipe.objects.get(id=id)
    serializedRecipe = RecipeFullSerializer(recipe, many=False)
    return Response(serializedRecipe.data)
