from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from.models import Recipe
from django.template import loader
from .forms import RecipeForm
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required


def index(request):
    return HttpResponse("Hello, world. You're at the Recipes Homepage.")

def get_recipe_by_id(request, recipe_id):
    recipe = get_object_or_404(Recipe, pk=recipe_id)
    context = {'recipe': recipe}
    template = loader.get_template("recipeKeeper/recipe_template.html")
    return HttpResponse(template.render(context, request))

@login_required
def add_recipe(request):
    if request.method == 'POST':
        form = RecipeForm(request.POST)
        
        if form.is_valid():
            recipe = form.save(commit=False)
            recipe.author = request.user
            recipe.save()

            # Get the ID of the newly added recipe
            new_recipe_id = recipe.pk
            return redirect('get_recipe_by_id', recipe_id=new_recipe_id)
    else:
        form = RecipeForm()
    context = {'form': form}
    template = loader.get_template("recipeKeeper/add_recipe.html")
    return HttpResponse(template.render(context, request))

def recipe_list(request):
    recipes = Recipe.objects.all()
    context = {'recipes': recipes}
    template = loader.get_template("recipeKeeper/recipe_list.html")
    return HttpResponse(template.render(context, request))