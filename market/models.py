from django.core.validators import MaxValueValidator, MinValueValidator, MinLengthValidator
from django.db import models
from solo.models import SingletonModel

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
class Recipes(models.Model):
    name = models.CharField(max_length=200)  # Название рецепта
    image = models.ImageField(upload_to='recipes/')  # Изображение рецепта
    description = models.TextField()  # Описание рецепта
    created_at = models.DateTimeField(auto_now_add=True)  # Дата создания рецепта
    updated_at = models.DateTimeField(auto_now=True)      # Дата последнего обновления

    class Meta:
        verbose_name = 'Рецепт'
        verbose_name_plural = 'Рецепты'
        ordering = ['name']  # Сортировка по названию

    def __str__(self):
        return self.name
class SocialMediaContact(SingletonModel):
    instagram = models.URLField()
    facebook = models.URLField()
    phone_number = models.CharField(
        max_length=20, validators=[MinLengthValidator(7)]
    )

    class Meta:
        verbose_name = 'Социальные сети и контакт'
        verbose_name_plural = 'Социальные сети и контакт'
