from django.contrib import admin
from coffee.models import Roaster, Country, CuppingNote, Coffee, Score, Critic, RoastLevel, Acidity
from import_export.admin import ImportExportActionModelAdmin
from import_export.widgets import ForeignKeyWidget, ManyToManyWidget
from import_export import fields, resources


# Register your models here.

class RoasterAdmin(admin.ModelAdmin):
    pass

class CountryAdmin(admin.ModelAdmin):
    pass

class CuppingNoteAdmin(admin.ModelAdmin):
    pass

class CriticAdmin(admin.ModelAdmin):
    pass

class ScoreAdmin(admin.ModelAdmin):
    pass

class CoffeeResource(resources.ModelResource):
    roaster = fields.Field(
        attribute='roaster',
        widget = ForeignKeyWidget(Roaster, field = 'name')
    )

    origin = fields.Field(
        attribute='origin',
        widget=ManyToManyWidget(Country,field='name',separator=', ')
    )

    roast_level = fields.Field(
        attribute='roast_level',
        widget = ForeignKeyWidget(RoastLevel, field = 'name')
    )

    acidity = fields.Field(
        attribute='acidity',
        widget = ForeignKeyWidget(Acidity, field = 'name')
    )

    cupping_notes = fields.Field(
        attribute='cupping_notes',
        widget=ManyToManyWidget(CuppingNote,field='name',separator=', ')
    )

    class Meta:
        model = Coffee
        import_id_fields = () # Empty tuple means don't use IDs
        fields = ('name','roaster','origin','roast_level','acidity','cupping_notes','created_on','last_modified','comments')



class CoffeeAdmin(ImportExportActionModelAdmin):
    resource_class = CoffeeResource
    list_display = ["name", "roaster", "created_on"]
    search_fields = ["name","roaster__name"]


admin.site.register(Roaster,RoasterAdmin)
admin.site.register(Country,CountryAdmin)
admin.site.register(CuppingNote,CuppingNoteAdmin)
admin.site.register(Coffee,CoffeeAdmin)
admin.site.register(Critic,CriticAdmin)
admin.site.register(Score,ScoreAdmin)