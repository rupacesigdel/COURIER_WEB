from django.contrib import admin
from .models import User, Order

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'is_customer', 'is_delivery_agent')
    list_filter = ('is_customer', 'is_delivery_agent')

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('customer', 'delivery_agent', 'status', 'price', 'created_at')
    list_filter = ('status', 'created_at')
    search_fields = ('customer__username', 'delivery_agent__username', 'pickup_address', 'dropoff_address')
