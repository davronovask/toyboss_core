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

from market.views import AboutView, HomeView, ProductView, ProductsDetailView, PublicationDetailView, PublicationView, RecipeDetailView, RecipesView
from django.conf.urls.i18n import i18n_patterns

urlpatterns = [
    path('admin/', admin.site.urls),
]

urlpatterns += i18n_patterns(
    path('set_language/', set_language, name='set_language'),
    path('', HomeView.as_view(), name='home'),
    path('about', AboutView.as_view(), name='about'),
    path('product', ProductView.as_view(), name='product'),
    path('product/<int:pk>', ProductsDetailView.as_view(), name='product_inner'),
    path('publications', PublicationView.as_view(), name='publications'),
    path('publications/<int:pk>', PublicationDetailView.as_view(), name='publications_inner'),
    path('recipes', RecipesView.as_view(), name='recipes'),  # Рецепты
    path('recipes/<int:pk>', RecipeDetailView.as_view(), name='recipes_inner'),
)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)