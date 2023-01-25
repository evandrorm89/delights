from django.urls import path, include

from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('account/', include('django.contrib.auth.urls'), name='login'),
    path('signup/', views.SignUp.as_view(), name='signup'),
    path('logout/', views.logout_request, name='logout'),
    path('menu/', views.MenuView.as_view(), name='menu'),
    path('menu/create', views.MenuItemCreate.as_view(), name='menu_create'),
    path('ingredients/list', views.IngredientsView.as_view(), name='ingredients'),
    path('ingredients/create', views.IngredientCreate.as_view(), name='ingredients_create'),
    path('ingredients/update/<pk>', views.IngredientUpdate.as_view(), name='ingredients_update'),
    path('purchases/list', views.PurchasesView.as_view(), name='purchases'),
    path('purchases/create', views.PurchaseCreate.as_view(), name='purchases_create'),
    path('recipe_requirement/list', views.RecipeRequirementView.as_view(), name='recipe_requirement'),
    path('recipe_requirement/create', views.RecipeRequirementCreate.as_view(), name='recipe_requirement_create'),
    path('finances/', views.finances, name='finances'),
]
