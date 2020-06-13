from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.views.generic.base import View

from .models import Order


# Create your views here.


class OrdersView(ListView):
    """Список заявок"""
    model = Order
    queryset = Order.objects.all()


class OrderDetailView(DetailView):
    model = Order
