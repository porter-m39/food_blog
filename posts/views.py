from django.shortcuts import render
from posts.models import Post, Tag
from django.views.generic import ListView
from django.db.models import Q

# Create your views here.

def post_index(request):
    posts = Post.objects.all().order_by("-created_on")
    tags = Tag.objects.all().order_by('name')
    context={
        "posts":posts,
        "tags":tags,
    }
    return render(request,"posts/index.html",context)

def post_tag(request, tag):
    posts = Post.objects.filter(
        tags__name__contains=tag
    ).order_by("-created_on")
    tags = Tag.objects.all().order_by('name')
    context = {
        "tag":tag,
        "posts":posts,
        "tags":tags
    }
    return render(request, "posts/tag.html",context)

def post_detail(request, slug):
    post = Post.objects.get(slug=slug)
    context = {
        "post":post,
    }
    return render(request, "posts/detail.html",context)