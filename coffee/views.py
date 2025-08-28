from django.shortcuts import render
from coffee.models import Roaster, Country, CuppingNote, Coffee
from django.db.models import Q

# Create your views here.

def coffee_index(request):
    coffees = Coffee.objects.all().order_by("-created_on")
    roasters = Roaster.objects.all().order_by("name")
    countries = Country.objects.all().order_by("name")
    context={
        "coffees":coffees,
        "roasters":roasters,
        "countries":countries,
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
    roasters = Roaster.objects.all().order_by("name")
    countries = Country.objects.all().order_by("name")
    context = {
        "roaster":roaster,
        "coffees":coffees,
        "roasters":roasters,
        "countries":countries,
    }
    return render(request, "coffee/roaster.html",context)

def coffee_origin(request,country):
    coffees = Coffee.objects.filter(
        origin__name__contains = country
    ).order_by("-created_on")
    roasters = Roaster.objects.all().order_by("name")
    countries = Country.objects.all().order_by("name")
    context = {
        "origin":country,
        "coffees": coffees,
        "roasters":roasters,
        "countries":countries,
    }
    return render(request, "coffee/origin.html", context)

def cupping_note(request, cupping_note):
    coffees = Coffee.objects.filter(
        cupping_notes__name__contains = cupping_note
    ).order_by("-created_on")
    roasters = Roaster.objects.all().order_by("name")
    countries = Country.objects.all().order_by("name")
    context = {
        "cupping_note":cupping_note,
        "coffees":coffees,
        "roasters":roasters,
        "countries":countries,
    }
    return render(request, "coffee/cupping_note.html",context)

def roast_level(request, roast_level):
    coffees = Coffee.objects.filter(
        roast_level__name=roast_level
    ).order_by("-created_on")
    roasters = Roaster.objects.all().order_by("name")
    countries = Country.objects.all().order_by("name")
    context = {
        "roast_level":roast_level,
        "coffees":coffees,
        "roasters":roasters,
        "countries":countries,
    }
    return render(request, "coffee/roast_level.html",context)

def acidity(request, acidity):
    coffees = Coffee.objects.filter(
        acidity__name = acidity
    ).order_by("-created_on")
    roasters = Roaster.objects.all().order_by("name")
    countries = Country.objects.all().order_by("name")
    context = {
        "acidity":acidity,
        "coffees":coffees,
        "roasters":roasters,
        "countries":countries,
    }
    return render(request, "coffee/acidity.html",context)

def processing(request, processing):
    coffees = Coffee.objects.filter(
        processing__name = processing
    ).order_by("-created_on")
    roasters = Roaster.objects.all().order_by("name")
    countries = Country.objects.all().order_by("name")
    context = {
        "processing":processing,
        "coffees":coffees,
        "roasters":roasters,
        "countries":countries,
    }
    return render(request, "coffee/processing.html",context)
