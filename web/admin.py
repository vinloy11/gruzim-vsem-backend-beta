from django.contrib import admin
from .models import Car, Category, Order, Reviews, User, Payment

admin.site.register(Car)
admin.site.register(Category)
admin.site.register(Order)
admin.site.register(Reviews)
admin.site.register(User)
admin.site.register(Payment)
