from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = "Categories"


class Drink(models.Model):
    image = models.ImageField()
    name = models.CharField(max_length=255)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Ingredient(models.Model):
    qty = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    drink = models.ForeignKey(Drink, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Step(models.Model):
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    drink = models.ForeignKey(Drink, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


