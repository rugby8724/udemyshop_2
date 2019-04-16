from django.shortcuts import render
from django.views import generic
from .models import Order
# Create your views here.

class SingleOrder(generic.DetailView):
    template_name = 'thanks.html'
    model = Order
