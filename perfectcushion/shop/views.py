from django.shortcuts import render
from django.views import generic
from .models import Product, Category
# Create your views here.

class ListProducts(generic.ListView):
    model = Product
    template_name = 'shop/category.html'

class SingleCategory(generic.DetailView):
    model = Category
