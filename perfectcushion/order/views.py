from django.shortcuts import render
from django.views import generic
from .models import Order, OrderItem
from django.http import Http404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

from braces.views import SelectRelatedMixin

from django.contrib.auth import get_user_model
User = get_user_model()

# Create your views here.

class SingleOrder(generic.DetailView):
    model = Order
    template_name = 'admin/order/thanks.html'

class OrderList(LoginRequiredMixin, generic.ListView):
    model = Order
    template_name = 'admin/order/order_list.html'


    def get_queryset(self):
        print(self.request.user)
        return Order.objects.filter(user=self.request.user)

    # def get_queryset(self):
    #     return Order.objects.filter(emailAddress = str(self.request.user.email))
