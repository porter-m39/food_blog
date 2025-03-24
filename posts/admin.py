from django.contrib import admin
from posts.models import Post, Tag
from import_export.admin import ImportExportActionModelAdmin

# Register your models here.


class TagAdmin(admin.ModelAdmin):
    def __str__(self):
        return self.name

class PostAdmin(ImportExportActionModelAdmin):
    prepopulated_fields = {"slug": ("title",)} #automatically generates slug as you write a post
    list_display = ["title", "created_on", "last_modified"]
    search_fields = ["title"]

admin.site.register(Tag,TagAdmin)
admin.site.register(Post,PostAdmin)