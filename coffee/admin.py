from django.contrib import admin
from coffee.models import Roaster, Country, CuppingNote, Coffee, Score, Critic # , RoastLevel, Acidity, (not registering roast level and acidity, for now)

# Register your models here.

class RoasterAdmin(admin.ModelAdmin):
    pass

class CountryAdmin(admin.ModelAdmin):
    pass

class CuppingNoteAdmin(admin.ModelAdmin):
    pass

class CoffeeAdmin(admin.ModelAdmin):
    pass

class CriticAdmin(admin.ModelAdmin):
    pass

class ScoreAdmin(admin.ModelAdmin):
    pass


admin.site.register(Roaster,RoasterAdmin)
admin.site.register(Country,CountryAdmin)
admin.site.register(CuppingNote,CuppingNoteAdmin)
admin.site.register(Coffee,CoffeeAdmin)
admin.site.register(Critic,CriticAdmin)
admin.site.register(Score,ScoreAdmin)