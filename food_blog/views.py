from django.http import HttpResponse
from django.shortcuts import render
from posts.models import Post
from coffee.models import Coffee
from django.db.models import Q

# def site_search(request):
#     query = request.GET.get("search_entry")
    
#     # Helper function to search all text fields in a model
#     def search_model(model, search_term):
#         q_objects = Q()
#         for field in model._meta.get_fields():
#             # Check if field is a text-based field (CharField, TextField, etc.)
#             if hasattr(field, 'get_internal_type') and field.get_internal_type() in (
#                 'CharField', 'TextField', 'EmailField', 'URLField', 'SlugField'
#             ):
#                 q_objects |= Q(**{f"{field.name}__icontains": search_term})
#         return model.objects.filter(q_objects).order_by("-created_on")
    
#     # Search both models
#     posts = search_model(Post, query)
#     coffees = search_model(Coffee, query)
    
#     context = {
#         "posts": posts,
#         "coffees": coffees,
#     }
#     return render(request, "search.html", context)