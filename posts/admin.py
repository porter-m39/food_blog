from django.contrib import admin
from posts.models import Post, Tag

# Register your models here.


class TagAdmin(admin.ModelAdmin):
    pass

class PostAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)} #automatically generates slug as you write a post

admin.site.register(Tag,TagAdmin)
admin.site.register(Post,PostAdmin)