from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models


class ProductCategory(models.Model):
    """Модель категории товара."""

    name = models.CharField(max_length=100, unique=True)

    class Meta:
        verbose_name_plural = 'Категории товаров'
        verbose_name = 'Категория товара'

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Категории товаров'
        verbose_name = 'Категория товара'

class Product(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='products/')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = 'Товары'
        verbose_name = 'Товар'

    def __str__(self):
        return self.name
