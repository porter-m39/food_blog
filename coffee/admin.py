from django.contrib import admin
from coffee.models import Roaster, Country, CuppingNote, Coffee, Score, Critic, RoastLevel, Acidity, Processing
from import_export.admin import ImportExportActionModelAdmin
from import_export.widgets import ForeignKeyWidget, ManyToManyWidget
from import_export import fields, resources

# the following two functions are from Deep Seek. They create manytomany and foreignkey classes upon import

class CreateForeignKeyWidget(ForeignKeyWidget):
    def clean(self, value, row=None, *args, **kwargs):
        # If the roaster doesn't exist, create it
        if value:
            obj, created = self.model.objects.get_or_create(
                name=value,  # Assumes 'name' is the field you're matching
                defaults={'name': value}  # Add other required fields if needed
            )
            return obj
        return super().clean(value, row, *args, **kwargs)
    
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

# Register your models here.

class RoasterAdmin(admin.ModelAdmin):
    pass

class CountryAdmin(admin.ModelAdmin):
    pass

class CuppingNoteAdmin(admin.ModelAdmin):
    pass

class CriticAdmin(admin.ModelAdmin):
    pass

class ScoreResource(resources.ModelResource):
    critic = fields.Field(
        attribute='critic',
        widget = CreateForeignKeyWidget(Critic, field = 'name')
    )

    coffee = fields.Field(
        attribute='coffee',
        widget = ForeignKeyWidget(Coffee, field = 'name')
    )

    class Meta:
        model = Score
        import_id_fields = () # Empty tuple means don't use IDs
        fields = ('critic','coffee','score','created_on')

class ScoreAdmin(ImportExportActionModelAdmin):
    resource_class = ScoreResource

class CoffeeResource(resources.ModelResource):
    roaster = fields.Field(
        attribute='roaster',
        widget = CreateForeignKeyWidget(Roaster, field = 'name')
    )

    origin = fields.Field(
        attribute='origin',
        widget=CreateManyToManyWidget(Country,field='name',separator=', ')
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
        widget=CreateManyToManyWidget(CuppingNote,field='name',separator=', ')
    )

    processing = fields.Field(
        attribute='processing',
        widget = CreateManyToManyWidget(Processing,field='name',separator=', ')
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