from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from.models import Recipe
from django.template import loader


def index(request):
    return HttpResponse("Hello, world. You're at the Recipes Homepage.")

def get_recipe_by_id(request, recipe_id):
    # Retrieve the recipe object by its ID
    recipe = get_object_or_404(Recipe, pk=recipe_id)
    # Pass the recipe object to the template context
    context = {'recipe': recipe}
    template = loader.get_template("recipeKeeper/recipe_template.html")
    # Render the template with the recipe details
    return HttpResponse(template.render(context, request))