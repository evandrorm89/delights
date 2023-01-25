from django.shortcuts import render
from django.http import HttpResponse
from django.views import generic
from .models import MenuItem, Ingredient, Purchase, RecipeRequirement
from .forms import MenuItemCreateForm, IngredientCreateForm, PurchaseCreateForm, RecipeCreateForm, IngredientUpdateForm
# Create your views here.
def home(request):
    context = {'name': 'Teste'}
    return render(request, 'django_delights/home.html', context)

class MenuView(generic.ListView):
    model = MenuItem

class IngredientsView(generic.ListView):
    model = Ingredient

class PurchasesView(generic.ListView):
    model = Purchase

class RecipeRequirementView(generic.ListView):
    model = RecipeRequirement

class MenuItemCreate(generic.CreateView):
    model = MenuItem
    template_name = 'django_delights/menu_item_create_form.html'
    form_class = MenuItemCreateForm

class IngredientCreate(generic.CreateView):
    model = Ingredient
    template_name = 'django_delights/ingredient_create_form.html'
    form_class = IngredientCreateForm

class IngredientUpdate(generic.UpdateView):
    model = Ingredient
    template_name = 'django_delights/ingredient_update_form.html'
    form_class = IngredientUpdateForm

class PurchaseCreate(generic.CreateView):
    model = Purchase
    template_name = 'django_delights/purchase_create_form.html'
    form_class = PurchaseCreateForm

class RecipeRequirementCreate(generic.CreateView):
    model = RecipeRequirement
    template_name ='django_delights/recipe_requirement_create_form.html'
    form_class = RecipeCreateForm

def finances(request):
    cost = 0
    ingredients = Ingredient.objects.all()
    for ingredient in ingredients:
        cost += ingredient.quantity * ingredient.unit_price

    purchases = Purchase.objects.all()
    revenue = 0
    # Tentar otimizar essa query depois
    for purchase in purchases:
        menu_item = MenuItem.objects.get(id=purchase.menu_item_id)
        revenue += menu_item.price
    context = {'cost':cost, 'revenue': revenue, 'profit': revenue - cost}
    return render(request, 'django_delights/finances.html', context)