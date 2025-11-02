from django.contrib import admin
from .models import Category, Product, CartItem, Order

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug', 'fabric_type', 'weave_type']
    prepopulated_fields = {'slug': ('name',)}
    list_filter = ['fabric_type', 'weave_type']

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'category', 'price', 'stock', 'featured', 'created_at']
    list_filter = ['category', 'featured', 'fabric_type', 'weave_type']
    search_fields = ['name', 'description']
    prepopulated_fields = {'slug': ('name',)}
    list_editable = ['price', 'stock', 'featured']

@admin.register(CartItem)
class CartItemAdmin(admin.ModelAdmin):
    list_display = ['product', 'quantity', 'session_key', 'created_at']
    list_filter = ['created_at']

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['id', 'customer_name', 'phone', 'total_price', 'created_at']
    list_filter = ['created_at']
    search_fields = ['customer_name', 'phone', 'email']