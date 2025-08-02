from django.contrib import admin
from posts.models import Post, Tag
from import_export.admin import ImportExportActionModelAdmin
from import_export.widgets import ManyToManyWidget
from import_export import fields, resources

# packages that I'll need if I want the display_tags to include links.
# from django.urls import reverse
# from django.utils.html import format_html

# Register your models here.


class TagAdmin(admin.ModelAdmin):
    def __str__(self):
        return self.name
    
class CreateManyToManyWidget(ManyToManyWidget):
    def clean(self, value, row=None, *args, **kwargs):
        if not value:
            return self.model.objects.none()
        
        values = [v.strip() for v in value.split(self.separator)]
        objs = []
        
        for val in values:
            obj, created = self.model.objects.get_or_create(
                name=val,
                defaults={'name': val}  # Add other required fields if needed
            )
            objs.append(obj)
            
        return objs
    
class PostResource(resources.ModelResource):
    tags = fields.Field(
        attribute = 'tags',
        widget=CreateManyToManyWidget(Tag, field='name', separator=', ')
    )

    class Meta:
        model = Post
        import_id_fields = ()  # Empty tuple means don't use IDs
        fields = ('title', 'slug', 'created_on', 'last_modified', 'tags', 'source', 'banner', 'body')


class PostAdmin(ImportExportActionModelAdmin):

    resource_class = PostResource  # This connects the resource to the admin
    prepopulated_fields = {"slug": ("title",)} #automatically generates slug as you write a post
    list_display = ["title", "created_on", "last_modified", "display_tags"]
    search_fields = ["title"]

    def display_tags(self, obj):
        return ", ".join([tag.name for tag in obj.tags.all()])
    

    #Below - some scrap work for making a display_tags which has links... not entirely working right now, would need to add stuff to the tags admin to get different links for each tag.

    # def display_tags(self, obj):
    #     #list = []
    #     for tag in obj.tags.all():
    #         link = reverse("admin:posts_tag_changelist")
    #         return format_html('<a href="{}">{}</a>', link, tag)

    
    display_tags.short_description = "Tags"

admin.site.register(Tag,TagAdmin)
admin.site.register(Post,PostAdmin)