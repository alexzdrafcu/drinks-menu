from .models import Category, Drink, Ingredient, Step
from django.contrib import admin

class IngredientInline(admin.TabularInline):
    model = Ingredient

class StepInline(admin.TabularInline):
    model = Step

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    pass

@admin.register(Drink)
class DrinkAdmin(admin.ModelAdmin):
    pass
    inlines = [IngredientInline,StepInline]

@admin.register(Ingredient)
class IngredientAdmin(admin.ModelAdmin):
    pass

@admin.register(Step)
class StepAdmin(admin.ModelAdmin):
    pass

