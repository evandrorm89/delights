from django.shortcuts import render
from django.http import HttpResponse
from django.views import generic
from .models import MenuItem, Ingredient, Purchase
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
    context = {'cost':cost, 'revenue': revenue}
    return render(request, 'django_delights/finances.html', context)