from django.shortcuts import render
from django.views import generic
from .models import Order
# Create your views here.

class SingleOrder(generic.DetailView):
    model = Order
    template_name = 'admin/order/thanks.html'
