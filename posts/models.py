from django.db import models

# auto slug imports
from django.db import models
from django.utils.text import slugify
from django.db.models.signals import pre_save
from django.dispatch import receiver
import uuid

def generate_unique_slug(title):
    slug = slugify(title)
    unique_slug = slug
    num = 1
    while Post.objects.filter(slug=unique_slug).exists():
        unique_slug = f'{slug}-{uuid.uuid4().hex[:4]}'  # or {num}
        num += 1
    return unique_slug

# Create your models here.

class Tag(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name

class Post(models.Model):
    title = models.CharField(max_length=225)
    body = models.TextField(blank=True) #body optional, in case you just want a headline or picture
    source = models.CharField(max_length=200, blank=True)
    source_link = models.URLField(max_length=200, blank=True)
    slug = models.SlugField(null=False,unique=True)
    created_on = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)
    tags = models.ManyToManyField("Tag", related_name="posts", blank=True) #tags are optional
    banner = models.ImageField(blank=True) #image not required. No longer include default.png

    def __str__(self):# this is an example of a method. no migrations needed when implementing.
        return self.title
    
@receiver(pre_save, sender=Post)
def generate_slug(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = generate_unique_slug(instance.title)