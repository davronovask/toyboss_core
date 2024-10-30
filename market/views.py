from django.core.paginator import Paginator
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from django.views.generic import TemplateView, ListView
from django.shortcuts import render
from market.models import Product, SocialMediaContact, AboutMe, ProductCategory, Recipes, Publication


class AboutView(TemplateView):
    template_name = 'about-company.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['about'] = AboutMe.objects.all()
        context['social_media'] = SocialMediaContact.objects.first()
        return context

class HomeView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['publications'] = Publication.objects.all().order_by('-created_at')[:2]
        return context

class ProductView(TemplateView ):
    template_name = 'product.html'

    def get_context_data(self, **kwargs):
        context = {
            'product_category_list':ProductCategory.objects.all(),
            'product_list': Product.objects.all(),
            'social_media': SocialMediaContact.objects.first()
        }
        return context


class ProductInnerView(TemplateView):
    template_name = 'product-inner.html'

    def product_inner(request, product_id):
        product = Product.objects.get(id=product_id)
        recipes = product.recipes.all()
        context = {
            'product': product,
            'recipes': recipes
        }
        return render(request, 'product-inner.html', context)
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        pk = self.kwargs.get('pk')
        product = get_object_or_404(Product, pk=pk)
        context['product'] = product
        context['social_media'] = SocialMediaContact.objects.first()
        return context


class PublicationView(TemplateView):
    template_name = 'publications.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        publication_list = Publication.objects.all()

        # Пагинация
        paginator = Paginator(publication_list, 3)
        page_number = self.request.GET.get('page')
        publications = paginator.get_page(page_number)

        context['publications'] = publications
        context['social_media'] = SocialMediaContact.objects.first()
        return context

class PublicationsInnerView(TemplateView):
    template_name = 'publications-inner.html'
    def publication_detail(request, publication_id):
        publication = get_object_or_404(Publication, id=publication_id)

        return render(request, 'publications-inner.html', {'publication': publication})

class RecipesView(TemplateView):
    template_name = 'recipes.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        # Получаем все рецепты
        recipe_list = Recipes.objects.all()

        # Пагинация
        paginator = Paginator(recipe_list, 3)
        page_number = self.request.GET.get('page', 1)
        recipes = paginator.get_page(page_number)

        context['recipes'] = recipes
        context['social_media'] = SocialMediaContact.objects.first()
        return context


class RecipesInnerView(TemplateView):
    template_name = 'recipes-inner.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        # Get the recipe_id from the URL
        recipe_id = self.kwargs.get('recipe_id')
        context['social_media'] = SocialMediaContact.objects.first()

        return context