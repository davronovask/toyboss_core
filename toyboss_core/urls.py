"""
URL configuration for toyboss_core project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from market.views import AboutView, HomeView, ProductView, ProductInnerView, PublicationsInnerView, PublicationsView, RecipesInnerView, RecipesView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/', HomeView.as_view(), name='home'),  # Главная страница
    path('about/', AboutView.as_view(), name='about'),  # О нас
    path('product/', ProductView.as_view(), name='product'),  # Продукция
    path('product/<int:pk>/', ProductInnerView.as_view(), name='product_inner'),  # Внутренняя страница продукта
    path('publications/', PublicationsView.as_view(), name='publications'),  # Публикации
    path('publications/<int:pk>/', PublicationsInnerView.as_view(), name='publications_inner'),# Внутренняя страница публикации
    path('recipes/', RecipesView.as_view(), name='recipes'),  # Рецепты
    path('recipes/<int:pk>/', RecipesInnerView.as_view(), name='recipes_inner'),  # Внутренняя страница рецепта
]
