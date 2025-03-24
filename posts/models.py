from django.db import models

# Create your models here.

class Tag(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name

class Post(models.Model):
    title = models.CharField(max_length=225)
    body = models.TextField(blank=True) #body optional, in case you just want a headline or picture
    source = models.CharField(max_length=200, blank=True)
    slug = models.SlugField(null=False,unique=True)
    created_on = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)
    tags = models.ManyToManyField("Tag", related_name="posts", blank=True) #tags are optional
    banner = models.ImageField(default='default.png',blank=True) #image not required, we have a fallback image. Images should be added to media directory

    def __str__(self):
        return self.title