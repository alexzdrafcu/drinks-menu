from rest_framework import serializers
from .models import Category, Drink, Ingredient, Step

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id','name']


class DrinkSerializer(serializers.ModelSerializer):
    class Meta:
        model = Drink
        fields = ['id','image','name','category']


class IngredientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ingredient
        fields = ['id','qty','name','drink']


class StepSerializer(serializers.ModelSerializer):
    class Meta:
        model = Step
        fields = ['id','name','description','drink']