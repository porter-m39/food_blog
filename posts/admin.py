from django.contrib import admin
from posts.models import Post, Tag

# Register your models here.


class TagAdmin(admin.ModelAdmin):
    pass

class PostAdmin(admin.ModelAdmin):
    pass

admin.site.register(Tag,TagAdmin)
admin.site.register(Post,PostAdmin)