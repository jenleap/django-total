from django.urls import path
from . import views

urlpatterns = [
    path('', views.getFoods, name='foods'),
    path('<str:id>/', views.getFood, name='foods'),
]