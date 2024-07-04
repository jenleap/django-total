from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import Recipe, Category
from .serializers import RecipeFullSerializer, RecipePartialSerializer


@api_view(['GET'])
def getRecipes(request):
    search_query = request.GET.get('search', None)
    category_name = request.GET.get('category', None)

    if search_query:
        recipes = Recipe.objects.filter(name__icontains=search_query)
    elif category_name:
        try:
            category = Category.objects.get(label=category_name)
            recipes = category.recipes.all()
        except Category.DoesNotExist:
            recipes = Recipe.objects.none()
    else:
        recipes = Recipe.objects.all()

    serializedRecipes = RecipePartialSerializer(recipes, many=True)
    return Response(serializedRecipes.data)

@api_view(['GET'])
def getRecipe(request, id):
    recipe = Recipe.objects.get(id=id)
    serializedRecipe = RecipeFullSerializer(recipe, many=False)
    return Response(serializedRecipe.data)

@api_view(['GET'])
def getRecipesByCategory(request):
    category_name = request.GET.get('category', None)
    if category_name:
        try:
            category = Category.objects.get(name=category_name)
            recipes = category.recipes.all()
        except Category.DoesNotExist:
            recipes = Recipe.objects.none()
    else:
        recipes = Recipe.objects.all()
    
    serialized_recipes = RecipePartialSerializer(recipes, many=True)
    return Response(serialized_recipes.data)

