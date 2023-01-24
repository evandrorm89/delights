from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('menu/', views.MenuView.as_view(), name='menu'),
    path('ingredients/list', views.IngredientsView.as_view(), name='ingredients'),
    path('purchases/list', views.PurchasesView.as_view(), name='purchases'),
    path('finances/', views.finances, name='finances'),
]
