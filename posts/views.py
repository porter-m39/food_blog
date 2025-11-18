from django.shortcuts import render
from posts.models import Post, Tag, Comment
from django.http import HttpResponseRedirect
from posts.forms import CommentForm

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
    form = CommentForm()
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = Comment(
                author = form.cleaned_data["author"],
                body = form.cleaned_data["body"],
                post = post
            )
            comment.save()
            return HttpResponseRedirect(request.path_info)
    comments = Comment.objects.filter(post=post)
    context = {
        "post":post,
        "comments":comments,
        "form":CommentForm(),
    }
    return render(request, "posts/detail.html",context)