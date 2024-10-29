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
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from django.views.i18n import set_language

from market.views import AboutView, HomeView, ProductView, ProductInnerView, PublicationsInnerView, PublicationView, RecipesInnerView, RecipesView
from django.conf.urls.i18n import i18n_patterns

urlpatterns = [
    path('admin/', admin.site.urls),
]

# Добавляем маршруты для мультиязычности
urlpatterns += i18n_patterns(
    path('set_language/', set_language, name='set_language'),
    path('', HomeView.as_view(), name='home'),  # Главная страница
    path('about/', AboutView.as_view(), name='about'),  # О нас
    path('product/', ProductView.as_view(), name='product'),  # Продукция
    path('product/<int:pk>/', ProductInnerView.as_view(), name='product_inner'),  # Внутренняя страница продукта
    path('publications/', PublicationView.as_view(), name='publications'),  # Публикации
    path('publications/<int:pk>/', PublicationsInnerView.as_view(), name='publications_inner'),  # Внутренняя страница публикации
    path('recipes/', RecipesView.as_view(), name='recipes'),  # Рецепты
    path('recipes/<int:pk>/', RecipesInnerView.as_view(), name='recipes_inner'),  # Внутренняя страница рецепта
)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)