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
