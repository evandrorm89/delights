from django.shortcuts import render
from django.http import HttpResponse
from django.views import generic
from .models import MenuItem
# Create your views here.
def index(request):
    return HttpResponse('Ok Ok Ratinho!')

class IndexView(generic.ListView):
    model = MenuItem