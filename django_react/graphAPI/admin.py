from django.contrib import admin

# Register your models here.

from .models import Category, Ingredient, URL, Customer, Order, OrderItem, OrderItemDetail


""" class Category(admin.ModelAdmin):
    list_display = ('name')


class Ingredient(admin.ModelAdmin):
    list_display = ('name', 'notes', 'category') """


admin.site.register(Category)
admin.site.register(Ingredient)
admin.site.register(URL)
admin.site.register(Customer)
admin.site.register(Order)
admin.site.register(OrderItem)
admin.site.register(OrderItemDetail)
