from django.test import TestCase
from django.urls import reverse
from market.models import ProductCategory, Publication, Recipes, SocialMediaContact, AboutMe


class PageAccessibilityTestCase(TestCase):
    def setUp(self):
        self.category = ProductCategory.objects.create(name='Test Category')
        self.publication = Publication.objects.create(
            name='Test Publication',
            content='Test Content',
            image='test_image.jpg'
        )
        self.recipes = Recipes.objects.create(
            name='Test Recipe',
            description='Test Description',
            image='test_image.jpg'
        )
        SocialMediaContact.objects.create(
            facebook='test_facebook',
        )
        AboutMe.objects.create(
            content='Test About Content',
            image='about_image.jpg'
        )

    def test_home_page_accessibility(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)

    def test_about_page_accessibility(self):
        response = self.client.get(reverse('about'))
        self.assertEqual(response.status_code, 200)

    def test_product_page_accessibility(self):
        response = self.client.get(reverse('product'))
        self.assertEqual(response.status_code, 200)

    def test_publication_page_accessibility(self):
        response = self.client.get(reverse('publications'))
        self.assertEqual(response.status_code, 200)

    def test_recipes_page_accessibility(self):
        response = self.client.get(reverse('recipes'))
        self.assertEqual(response.status_code, 200)

