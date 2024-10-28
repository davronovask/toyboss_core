from modeltranslation.translator import register, TranslationOptions
from market.models import Publication, Recipes, AboutMe, Product

@register(Product)
class ProductTranslationOptions(TranslationOptions):
    fields = ('name', 'description',)

@register(Publication)
class PublicationTranslationOptions(TranslationOptions):
    fields = ('name', 'content',)

@register(Recipes)
class RecipeTranslationOptions(TranslationOptions):
    fields = ('name', 'description',)

@register(AboutMe)
class AboutUsTranslationOptions(TranslationOptions):
    fields = ('content', 'name')