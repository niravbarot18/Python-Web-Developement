from django.shortcuts import render
import requests
from .models import *
# Create your views here.

def index(request):
    url=requests.get("https://dummyjson.com/recipes")
    mydata=url.json()
    context={
        "recipe": mydata["recipes"]
    }
    return render (request,"index.html",context)

def allrecipe(request):
    url=requests.get("https://dummyjson.com/recipes")
    mydata=url.json()
    context={
        "recipe":mydata["recipes"]
    }
    return render (request,"allrecipe.html", context)

def recipe(request, id):
    # Selected recipe
    recipe_detail = requests.get(f"https://dummyjson.com/recipes/{id}").json()

    # All recipes
    recipes = requests.get("https://dummyjson.com/recipes").json()

    context = {
        "recipedetails": recipe_detail,
        "recipes": recipes["recipes"]
    }

    return render(request, "recipe.html", context)

def contact(request):
    if request.method == "POST":
        name=request.POST.get("name")
        email=request.POST.get("_replyto")
        message=request.POST.get("message")

        print(name)
        print(email)
        print(message)

        insertquery=Contact(name=name,email=email,message=message)
        insertquery.save()


    return render (request,"contact.html")

def search(request):
    if request.method == "POST":
        query=request.POST.get("query")
        url=requests.get(f"https://dummyjson.com/recipes/search?q={query}")
        response=url.json()
        context={
            "recipe":response["recipes"]
        }
        return render (request,"search.html",context)
    return render (request,"search.html")


def sign_in(request):
    return render (request,"sign_in.html")

def sign_up(request):
    return render (request,"sign_up.html")

