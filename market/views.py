from django.http import HttpResponse
from django.views.generic import TemplateView, FormView
from django.shortcuts import render


class AboutView(TemplateView):
    template_name = 'about-company.html'

class HomeView(TemplateView):
    template_name = 'index.html'

class ProductView(TemplateView):
    template_name = 'product.html'

class ProductInnerView(TemplateView):
    template_name = 'product-inner.html'

class PublicationsView(TemplateView):
    template_name = 'publications.html'

class PublicationsInnerView(TemplateView):
    template_name = 'publications-inner.html'

class RecipesView(TemplateView):
    template_name = 'recipes.html'

class RecipesInnerView(TemplateView):
    template_name = 'recipes-inner.html'