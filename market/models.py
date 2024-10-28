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
    """Модель рецепта."""
    name_ru = models.CharField(max_length=200)
    name_en = models.CharField(max_length=200)
    image = models.ImageField(upload_to='recipes/')  # Изображение рецепта
    description_ru = models.TextField()  # Описание рецепта
    description_en = models.TextField()
    categories = models.ManyToManyField(ProductCategory, related_name='recipes')  # Связь многие ко многим

    class Meta:
        verbose_name = 'Рецепт'
        verbose_name_plural = 'Рецепты'
        ordering = ['name']  # Сортировка по названию

    def __str__(self):
        return self.name

class Product(models.Model):
    name_ru = models.CharField(max_length=255)
    name_en = models.CharField(max_length=255)
    description_ru = models.TextField()
    description_en = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='product/')
    category = models.ForeignKey(ProductCategory, on_delete=models.CASCADE, related_name='products')  # Внешний ключ на категорию
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = 'Товары'
        verbose_name = 'Товар'

    def __str__(self):
        return self.name


class AboutMe(models.Model):
    name_ru = models.CharField(max_length=100, null=True, blank=True)
    name_en = models.CharField(max_length=100, null=True, blank=True)
    content_ru = RichTextField()
    content_en = RichTextField()
    image = models.ImageField(null=True, blank=True)  # Image is optional

    class Meta:
        verbose_name = 'O нас'
        verbose_name_plural = 'О нас'

    def __str__(self):
        return self.name if self.name else "About Me Section"

class Publication(models.Model):
    """Модель публикации."""

    name_ru = models.CharField(max_length=200)
    name_en = models.CharField(max_length=200)
    content_ru = models.TextField()
    content_en = models.TextField()
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
