from ckeditor.fields import RichTextField
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

class Recipes(models.Model):
    """Model for recipes."""
    name = models.CharField(max_length=200)
    description = models.TextField()
    ingredients = models.TextField()
    directions = models.TextField()
    image = models.ImageField(upload_to='recipes/')
    categories = models.ManyToManyField(ProductCategory)

    def __str__(self):
        return self.name
    class Meta:
        verbose_name = 'Рецепт'
        verbose_name_plural = 'Рецепты'
        ordering = ['name']

    def __str__(self):
        return self.name

class Product(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='product/')
    category = models.ForeignKey(ProductCategory, on_delete=models.CASCADE, related_name='products')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    composition = models.TextField(blank=True)

    class Meta:
        verbose_name_plural = 'Товары'
        verbose_name = 'Товар'

    def __str__(self):
        return self.name


class AboutMe(models.Model):
    name = models.CharField(max_length=100, null=True, blank=True)
    content = RichTextField()
    image = models.ImageField(null=True, blank=True)

    class Meta:
        verbose_name = 'O нас'
        verbose_name_plural = 'О нас'

    def __str__(self):
        return self.name if self.name else "About Me Section"

class Publication(models.Model):
    """Модель публикации."""

    name = models.CharField(max_length=200)
    content = models.TextField()
    image = models.ImageField(upload_to='publications/')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Публикация'
        verbose_name_plural = 'Публикации'
        ordering = ['-created_at']

    def __str__(self):
        return self.name


class SocialMediaContact(SingletonModel):
    instagram = models.URLField()
    facebook = models.URLField()
    phone_number = models.URLField()


    class Meta:
        verbose_name = 'Социальные сети и контакт'
        verbose_name_plural = 'Социальные сети и контакт'
