from django.contrib import admin
from market.models import Product, ProductCategory

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name']

@admin.register(ProductCategory)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name']git config user.namegit add <название-файлов>