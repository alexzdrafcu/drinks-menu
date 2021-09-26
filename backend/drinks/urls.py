from django.urls import include, path
from rest_framework import routers
from . import views
from .views import CategoryViewset, DrinkViewset, IngredientViewset, StepViewset

router = routers.DefaultRouter()
router.register('categories', CategoryViewset)
router.register('ingredients', IngredientViewset)
router.register('steps', StepViewset)
router.register('drinks', DrinkViewset)
urlpatterns = [
    path('', include(router.urls)),
    path('get_drink_by_category/<category_id>',views.get_drink_by_category),
    path('get_ingredients_by_drink/<drink_id>',views.get_ingredients_by_drink),
    path('get_steps_by_drink/<drink_id>',views.get_steps_by_drink),
]