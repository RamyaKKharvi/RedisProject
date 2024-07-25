from django.shortcuts import render
from .models import Recipe
# install settings to use cache TTL
from django.conf import settings
from django.core.cache.backends.base import DEFAULT_TIMEOUT
from django.views.decorators.cache import cache_page
from django.core.cache import cache

# import (or get) cache TTL from settings
CACHE_TTL = getattr(settings, 'CACHE_TTL', DEFAULT_TIMEOUT)


def get_recipe(filter_recipe=None):
    if filter_recipe:
        print("DATA COMING FROM DB")
        recipes = Recipe.objects.filter(name__contains=filter_recipe)
    else:
        recipes = Recipe.objects.all()
    return recipes


def home(request):
    filter_recipe = request.GET.get("recipe")
    print("DATA COMING FROM CACHE")
    if cache.get(filter_recipe):
        recipe = cache.get(filter_recipe)
    else:
        if filter_recipe:
            recipe = get_recipe(filter_recipe)
            cache.set(filter_recipe, recipe)
        else:
            recipe = get_recipe()
    context = {"recipe": recipe}
    return render(request, template_name="home.html", context=context)


def show(request, id):
    if cache.get(id):
        print('Data coming from cache')
        recipe = cache.get(id)
    else:
        print('Data coming from DB')

        recipe = Recipe.objects.get(id=id)
    context = {'recipe': recipe}
    return render(request, template_name='show.html', context=context)
