from django.contrib import admin
from market.models import Product, ProductCategory, Recipes, SocialMediaContact, Publication, AboutMe
from solo.admin import SingletonModelAdmin
from modeltranslation.admin import TranslationAdmin

@admin.register(Product)
class ProductAdmin(TranslationAdmin):
    list_display = ['name']

@admin.register(ProductCategory)
class ProductCategoryAdmin(admin.ModelAdmin):
    list_display = ['name']

@admin.register(Publication)
class PublicationAdmin(TranslationAdmin):
    list_display = ['name']

@admin.register(Recipes)
class RecipesAdmin(TranslationAdmin):
    list_display = ['name']

@admin.register(AboutMe)
class AboutMeAdmin(TranslationAdmin):
    list_display = ['content']
# class SocialMediaContactAdmin(admin.ModelAdmin):
#     list_display = ('instagram', 'facebook', 'phone_number')

admin.site.register(SocialMediaContact, SingletonModelAdmin)