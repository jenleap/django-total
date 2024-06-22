from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import Food
from .serializers import FoodSerializer


@api_view(['GET'])
def getFoods(request):
    foods = Food.objects.all()
    serializedFoods = FoodSerializer(foods, many=True)
    return Response(serializedFoods.data)

@api_view(['GET'])
def getFood(request, id):
    food = Food.objects.get(id=id)
    serializedFood = FoodSerializer(food, many=False)
    return Response(serializedFood.data)
