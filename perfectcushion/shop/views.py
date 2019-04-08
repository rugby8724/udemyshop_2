from django.shortcuts import render
from django.views import generic
from django.db.models import Q
from .models import Product, Category
from django.core.paginator import Paginator, EmptyPage, InvalidPage
# Create your views here.

class ListProducts(generic.ListView):
    model = Product
    context_object_name = 'products'
    paginate_by = 6
    queryset = Product.objects.all()


class SingleCategory(generic.DetailView):
    model = Category

class SingleProduct(generic.DetailView):
    model = Product
