from django.shortcuts import render
from django.views import generic
from .models import Product, Category
# Create your views here.

class ListProducts(generic.ListView):
    model = Product


class SingleCategory(generic.DetailView):
    model = Category

class SingleProduct(generic.DetailView):
    model = Product
