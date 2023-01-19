from django.db import models

# Create your models here.
class Ingredient(models.Model):
    name = models.CharField(max_length=200)
    quantity = models.IntegerField(default=0)
    unit = models.CharField(default='kg', max_length=200)
    unit_price = models.FloatField()

    def __str__(self):
        return self.name

class MenuItem(models.Model):
    title = models.CharField(max_length=200)
    price = models.FloatField()

    def __str__(self):
        return self.title

class RecipeRequirement(models.Model):
    menu_item = models.ForeignKey(MenuItem, on_delete=models.CASCADE)
    ingredient = models.ForeignKey(Ingredient, on_delete=models.CASCADE)
    quantity = models.FloatField()

    def __str__(self):
        return f'{self.quantity} {self.ingredient.unit} of {self.ingredient.name} to create {self.menu_item.title}'

class Purchase(models.Model):
    menu_item = models.ForeignKey(MenuItem, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.menu_item.title} purchased at {self.timestamp}'