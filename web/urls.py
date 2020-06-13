from django.urls import path

from . import views

urlpatterns = [
    path("", views.OrdersView.as_view()),
    path("orders/<int:pk>/", views.OrderDetailView.as_view(), name="order_details")
]
