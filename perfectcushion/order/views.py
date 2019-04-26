from django.shortcuts import render
from django.views import generic
from .models import Order, OrderItem
from django.http import Http404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

from django.contrib.auth import get_user_model
User = get_user_model()

# Create your views here.

class SingleOrder(generic.DetailView):
    model = Order
    template_name = 'admin/order/thanks.html'

class OrderList(LoginRequiredMixin, generic.ListView):
    model = Order
    template_name = 'admin/order/order_list.html'


class OrderDetail(LoginRequiredMixin, generic.DetailView):
    model = OrderItem



# @login_required()
# def orderHistory(request):
# 	if request.user.is_authenticated:
# 		email = User.objects.get(email__iexact=self.)
# 		order_details = Order.objects.filter(emailAddress=email)
# 	return render(request, 'admin/order/order_list.html', {'order_details':order_details})
