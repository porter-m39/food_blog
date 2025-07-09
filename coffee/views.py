from django.shortcuts import render
from coffee.models import Roaster, Country, CuppingNote, Coffee

# Create your views here.

def coffee_index(request):
    coffees = Coffee.objects.all().order_by("-created_on")
    context={
        "coffees":coffees,
    }
    return render(request,"coffee/index.html",context) 

def coffee_detail(request, pk):
    coffee = Coffee.objects.get(pk=pk)
    context = {
        "coffee" : coffee
    }
    return render(request,"coffee/detail.html",context)

def coffee_roaster(request, roaster):
    coffees = Coffee.objects.filter(
        roaster__name=roaster
    ).order_by("-created_on")
    context = {
        "roaster":roaster,
        "coffees":coffees,
    }
    return render(request, "coffee/roaster.html",context)

def coffee_origin(request,country):
    coffees = Coffee.objects.filter(
        origin__name__contains = country
    ).order_by("-created_on")
    context = {
        "origin":country,
        "coffees": coffees,
    }
    return render(request, "coffee/origin.html", context)
