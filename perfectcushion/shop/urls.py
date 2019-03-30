from django.urls import path
from . import views

app_name='shop'

urlpatterns = [
    path('', views.ListProducts.as_view(), name='allprodcat'),
    path('<slug:<slug>/', views.SingleCategory.as_view(), name='productsbycategory'),
]
