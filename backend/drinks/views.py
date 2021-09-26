from .models import Category, Drink, Ingredient, Step
from .serializers import CategorySerializer, DrinkSerializer, IngredientSerializer, StepSerializer
from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.decorators import api_view
from rest_framework.response import Response


class CategoryViewset(viewsets.ModelViewSet):
    serializer_class = CategorySerializer
    queryset = Category.objects.all()

class DrinkViewset(viewsets.ModelViewSet):
    serializer_class = DrinkSerializer
    queryset = Drink.objects.all()

class IngredientViewset(viewsets.ModelViewSet):
    serializer_class = IngredientSerializer
    queryset = Ingredient.objects.all()

class StepViewset(viewsets.ModelViewSet):
    serializer_class = StepSerializer
    queryset = Step.objects.all()


@api_view(['GET'])
def get_drink_by_category(request, category_id):
    drinks = Drink.objects.filter(category__id=category_id)
    serialized_data = DrinkSerializer(drinks, many=True)

    return Response(serialized_data.data)


@api_view(['GET'])
def get_ingredients_by_drink(request, drink_id):
    ingredients = Ingredient.objects.filter(drink__id=drink_id)
    serialized_data = IngredientSerializer(ingredients, many=True)

    return Response(serialized_data.data)


@api_view(['GET'])
def get_steps_by_drink(request, drink_id):
    steps = Step.objects.filter(drink__id=drink_id)
    serialized_data = StepSerializer(steps, many=True)

    return Response(serialized_data.data)
