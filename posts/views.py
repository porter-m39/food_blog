from django.shortcuts import render
from posts.models import Post, Tag
from django.views.generic import ListView
from django.db.models import Q

# Create your views here.

def post_index(request):
    posts = Post.objects.all().order_by("-created_on")
    context={
        "posts":posts,
    }
    return render(request,"posts/index.html",context)

def post_tag(request, tag):
    posts = Post.objects.filter(
        tags__name__contains=tag
    ).order_by("-created_on")
    context = {
        "tag":tag,
        "posts":posts,
    }
    return render(request, "posts/tag.html",context)

def post_detail(request, slug):
    post = Post.objects.get(slug=slug)
    context = {
        "post":post,
    }
    return render(request, "posts/detail.html",context)

def post_search(request):
    query = request.GET.get("search_entry")
    posts = Post.objects.filter(
        Q(title__icontains=query) | Q(body__icontains=query)
    ).order_by("-created_on")
    context = {
        "posts":posts,
    }
    return render(request, "posts/search.html",context)