from django.contrib import admin
from posts.models import Post, Tag
from import_export.admin import ImportExportActionModelAdmin
from django.urls import reverse
from django.utils.html import format_html

# Register your models here.


class TagAdmin(admin.ModelAdmin):
    def __str__(self):
        return self.name

class PostAdmin(ImportExportActionModelAdmin):
    prepopulated_fields = {"slug": ("title",)} #automatically generates slug as you write a post
    list_display = ["title", "created_on", "last_modified", "display_tags"]
    search_fields = ["title"]

    def display_tags(self, obj):
        list = []
        for tag in obj.tags.all():
            list.append(tag)
        return list
    

    #Below - some scrap work for making a display_tags which has links... not entirely working right now, would need to add stuff to the tags admin to get different links for each tag.

    # def display_tags(self, obj):
    #     #list = []
    #     for tag in obj.tags.all():
    #         link = reverse("admin:posts_tag_changelist")
    #         return format_html('<a href="{}">{}</a>', link, tag)

    
    display_tags.short_description = "Tags"

admin.site.register(Tag,TagAdmin)
admin.site.register(Post,PostAdmin)