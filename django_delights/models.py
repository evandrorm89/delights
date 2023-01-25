from django.db import models

# Create your models here.
class Ingredient(models.Model):
    name = models.CharField(max_length=200)
    quantity = models.IntegerField(default=0)
    unit = models.CharField(default='kg', max_length=200)
    unit_price = models.FloatField()

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return '/django_delights/ingredients/list'

class MenuItem(models.Model):
    title = models.CharField(max_length=200)
    price = models.FloatField()

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return '/django_delights/menu'

class RecipeRequirement(models.Model):
    menu_item = models.ForeignKey(MenuItem, on_delete=models.CASCADE)
    ingredient = models.ForeignKey(Ingredient, on_delete=models.CASCADE)
    quantity = models.FloatField()

    def __str__(self):
        return f'{self.quantity} {self.ingredient.unit} of {self.ingredient.name} to create {self.menu_item.title}'

    def get_absolute_url(self):
        return '/django_delights/recipe_requirement/list'

class Purchase(models.Model):
    menu_item = models.ForeignKey(MenuItem, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.menu_item.title} purchased at {self.timestamp}'

    def get_absolute_url(self):
        return '/django_delights/purchases/list'

    # check if there are enough ingredients for a purchase to be made
    def save(self):
        menu_item_id = self.menu_item_id
        recipe_requirements = RecipeRequirement.objects.filter(menu_item_id=menu_item_id)
        for requirement in recipe_requirements:
            ingredient = Ingredient.objects.get(id=requirement.ingredient_id)
            if requirement.quantity > ingredient.quantity:
                return f'There is not enough {ingredient.name}!'
        super().save()