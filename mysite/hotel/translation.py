from .models import Hotel, City
from  modeltranslation.translator import TranslationOptions, register



@register(Hotel)
class ActorTranslationOptions(TranslationOptions):
    fields = ('hotel_name', 'description')



@register(City)
class CountryTranslationOptions(TranslationOptions):
    fields = ('city_name',)