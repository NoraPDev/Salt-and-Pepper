from django.shortcuts import render
from main.models import Recipe
from main.forms import RecipeForm

# Create your views here.
def home(request):
    context = {
        'recipes': Recipe.objects.order_by('-id')[0:3]
    }
    return render(request, "home.html", context)

def recipe_details(request, id):
    context = {
        'recipe': Recipe.objects.get(id=id)
    }
    return render(request, "recipe-details.html", context)

def recipe_list(request):
    context = {
        "recipes": Recipe.objects.all(),
        "form": RecipeForm()
    }
    return render(request, "recipe-list.html", context)

def new_recipe(request):
    recipe_form = RecipeForm(request.POST)

    form_valid = recipe_form.is_valid()

    if form_valid:
        recipe_form.save()

    context = {
        "form_valid": form_valid
    }

    return render(request, "new-recipe.html", context)

def delete_recipe(request, id):
    Recipe.objects.filter(id=id).delete()
    context = {
        "recipes": Recipe.objects.all(),
        "form": RecipeForm()
    }
    return render(request, "recipe-list.html", context)

def update_recipe(request, id):
    recipe = Recipe.objects.filter(id=id)

    context = {
        "recipes": Recipe.objects.all(),
        "form": RecipeForm(instance=recipe[0]),
        "recipe_id": recipe[0].id
    }
    return render(request, "update-recipe.html", context)

def edit_recipe(request):
    recipe_form = RecipeForm(request.POST)

    print(request.POST)

    form_valid = recipe_form.is_valid()

    if form_valid:
        recipe= Recipe.objects.get(id=request.POST["id"])
        recipe.name = request.POST["name"]
        recipe.photo = request.POST["photo"]
        recipe.short_description = request.POST["short_description"]
        recipe.preparation_guide = request.POST["preparation_guide"]
        recipe.difficulty = request.POST["difficulty"]
        recipe.ideal_for = request.POST["ideal_for"]
        recipe.preparation_time = request.POST["preparation_time"]
        recipe.ingredients = request.POST["ingredients"]
        recipe.save()

    return render(request, "edit-recipe.html", { "form_valid": form_valid })