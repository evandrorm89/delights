from django import forms
from .models import MenuItem, Ingredient, Purchase, RecipeRequirement

class MenuItemCreateForm(forms.ModelForm):
    class Meta:
        model = MenuItem
        fields = ('title', 'price')

class IngredientCreateForm(forms.ModelForm):
    class Meta:
        model = Ingredient
        fields = ('name', 'quantity', 'unit', 'unit_price')

class IngredientUpdateForm(forms.ModelForm):
    class Meta:
        model = Ingredient
        fields = ('name', 'quantity', 'unit', 'unit_price')

class PurchaseCreateForm(forms.ModelForm):
    class Meta:
        model = Purchase
        fields = ('menu_item',)

class RecipeCreateForm(forms.ModelForm):
    class Meta:
        model = RecipeRequirement
        fields = ('menu_item', 'ingredient', 'quantity')
