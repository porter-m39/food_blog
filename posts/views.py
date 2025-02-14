from django.shortcuts import render
from posts.models import Post, Tag

# Create your views here.

def post_index(request):
    posts = Post.objects.all().order_by("-created_on")
    context={
        "posts":posts,
    }
    return render(request,"posts/index.html",context)