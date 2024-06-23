from django.urls import path
from . import views

urlpatterns = [
    path('', views.getRecipes, name='recipes'),
    path('<str:id>/', views.getRecipe, name='recipes'),
]