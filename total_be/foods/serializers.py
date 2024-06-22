from rest_framework import serializers
from .models import Food, Measure

class MeasureSerializer(serializers.ModelSerializer):
    class Meta:
        model = Measure
        fields = '__all__'

class FoodSerializer(serializers.ModelSerializer):
    measures = MeasureSerializer(many=True)
    
    class Meta:
        model = Food
        fields = '__all__'