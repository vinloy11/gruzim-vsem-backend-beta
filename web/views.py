from django.shortcuts import render
from django.views.generic.list import View

from .models import Order
# Create your views here.


class OrdersView(View):
    """Список заявок"""
    def get(self, request):
        orders = Order.objects.all()
        return render(request, "orders.html", {"orders_list": orders})
