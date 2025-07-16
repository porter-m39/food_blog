from django.shortcuts import render
from coffee.models import Roaster, Country, CuppingNote, Coffee
from django.db.models import Q

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

def cupping_note(request, cupping_note):
    coffees = Coffee.objects.filter(
        cupping_notes__name__contains = cupping_note
    ).order_by("-created_on")
    context = {
        "cupping_note":cupping_note,
        "coffees":coffees,
    }
    return render(request, "coffee/cupping_note.html",context)

def roast_level(request, roast_level):
    coffees = Coffee.objects.filter(
        roast_level__name=roast_level
    ).order_by("-created_on")
    context = {
        "roast_level":roast_level,
        "coffees":coffees,
    }
    return render(request, "coffee/roast_level.html",context)

def acidity(request, acidity):
    coffees = Coffee.objects.filter(
        acidity__name = acidity
    ).order_by("-created_on")
    context = {
        "acidity":acidity,
        "coffees":coffees,
    }
    return render(request, "coffee/acidity.html",context)

def coffee_search(request):
    query = request.GET.get("search_entry")
    
    # Helper function to search all text fields in a model
    def search_model(model, search_term):
        q_objects = Q()
        for field in model._meta.get_fields():
            # Check if field is a text-based field (CharField, TextField, etc.)
            if hasattr(field, 'get_internal_type') and field.get_internal_type() in (
                'CharField', 'TextField', 'EmailField', 'URLField', 'SlugField'
            ):
                q_objects |= Q(**{f"{field.name}__icontains": search_term})
        return model.objects.filter(q_objects).order_by("-created_on")
    
    # Search both models
    coffees = search_model(Coffee, query)
    
    context = {
        "coffees": coffees,
    }
    return render(request, "coffee/search.html", context)

