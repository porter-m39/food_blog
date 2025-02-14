from django.db import models

# Create your models here.

class Tag(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name

class Post(models.Model):
    title = models.CharField(max_length=225)
    body = models.TextField()
    slug = models.SlugField(null=False,unique=True)
    created_on = models.DateTimeField(auto_now=True)
    last_modified = models.DateTimeField(auto_now=True)
    tags = models.ManyToManyField("Tag", related_name="posts")

    def __str__(self):
        return self.title