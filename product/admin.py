from django.contrib import admin
from .models import Cart, CartItem, Category, Product


class CartAdmin(admin.ModelAdmin):
    list_display = ('id', 'user')
    search_fields = ['id', "user__username"]


class CartItemAdmin(admin.ModelAdmin):
    list_display = ('id', 'cart', "product", 'quantity')
    search_fields = ['id', 'cart__id', 'cart__user__username', 'product__name']


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    search_fields = ['id', "name"]


class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', "price", "discount")
    search_fields = ['id', "name"]


# Register your models here.
admin.site.register(Cart, CartAdmin)
admin.site.register(CartItem, CartItemAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Product, ProductAdmin)
