from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views import generic
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import logout
from django.urls import reverse_lazy
from django.contrib.auth.forms import UserCreationForm

from .models import MenuItem, Ingredient, Purchase, RecipeRequirement
from .forms import MenuItemCreateForm, IngredientCreateForm, PurchaseCreateForm, RecipeCreateForm, IngredientUpdateForm
# Create your views here.
@login_required
def home(request):
    context = {'name': request.user}
    return render(request, 'django_delights/home.html', context)

class MenuView(LoginRequiredMixin, generic.ListView):
    model = MenuItem

class IngredientsView(LoginRequiredMixin, generic.ListView):
    model = Ingredient

class PurchasesView(LoginRequiredMixin, generic.ListView):
    model = Purchase

class RecipeRequirementView(LoginRequiredMixin, generic.ListView):
    model = RecipeRequirement

class SignUp(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'

class MenuItemCreate(LoginRequiredMixin, generic.CreateView):
    model = MenuItem
    template_name = 'django_delights/menu_item_create_form.html'
    form_class = MenuItemCreateForm

class IngredientCreate(LoginRequiredMixin, generic.CreateView):
    model = Ingredient
    template_name = 'django_delights/ingredient_create_form.html'
    form_class = IngredientCreateForm

class IngredientUpdate(LoginRequiredMixin, generic.UpdateView):
    model = Ingredient
    template_name = 'django_delights/ingredient_update_form.html'
    form_class = IngredientUpdateForm

class PurchaseCreate(LoginRequiredMixin, generic.CreateView):
    model = Purchase
    template_name = 'django_delights/purchase_create_form.html'
    form_class = PurchaseCreateForm

class RecipeRequirementCreate(LoginRequiredMixin, generic.CreateView):
    model = RecipeRequirement
    template_name ='django_delights/recipe_requirement_create_form.html'
    form_class = RecipeCreateForm

@login_required
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

def logout_request(request):
    logout(request)
    return redirect('home')
