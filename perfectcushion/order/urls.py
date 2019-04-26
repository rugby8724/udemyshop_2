from django.urls import path
from . import views

app_name = 'order'

urlpatterns = [
    path('thanks/<int:pk>/', views.SingleOrder.as_view(), name='thanks'),
    path('history/', views.OrderList.as_view(), name='order_history'),
    # path('history/', views.orderHistory, name='order_history'),
]
