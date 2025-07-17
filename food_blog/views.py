from django.http import HttpResponse
from django.shortcuts import render
from posts.models import Post
from coffee.models import Coffee
from django.db.models import Q

def site_search(request):
    query = request.GET.get("search_entry")

    posts = Post.objects.filter(
        Q(title__icontains=query) | Q(body__icontains=query) | Q(tags__name__icontains=query) | Q(source__icontains=query)
    ).order_by("-created_on").distinct()

    coffees = Coffee.objects.filter(
        Q(name__icontains=query) | Q(roaster__name__icontains=query) | Q(origin__name__icontains=query) | Q(cupping_notes__name__icontains=query) | Q(comments__icontains=query)
    ).order_by("-created_on").distinct()
    
    # context passes certain variables on for the html file to render
    context = {
        "posts": posts,
        "coffees": coffees,
        "query":query,
    }
    return render(request, "search.html", context)