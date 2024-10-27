from django.contrib import admin
from market.models import Product, ProductCategory, Recipes, SocialMediaContact
from solo.admin import SingletonModelAdmin
@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name']

@admin.register(ProductCategory)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name']

@admin.register(SocialMediaContact)
class SocialMediaContactAdmin(admin.ModelAdmin):
    list_display = ['instagram', 'facebook', 'phone_number']

# @admin.register(Recipes)
# class RecipesAdmin(admin.ModelAdmin):
#     list_display = ['name']

admin.site.register(SocialMediaContact, SingletonModelAdmin)