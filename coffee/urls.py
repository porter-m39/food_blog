# posts/urls.py

from django.urls import path
from . import views

app_name = 'coffee' #this designates that the names of the URLs below belong to the coffees app. So in the html files, write coffee:<name>

urlpatterns = [
    path("", views.coffee_index,name="coffee_index"),
    path('<slug:slug>', views.coffee_detail, name="coffee_detail"),
    path("roaster/<roaster>/",views.coffee_roaster,name="coffee_roaster"),
    path("origin/<country>/",views.coffee_origin,name="coffee_origin"),
    path("cupping_note/<cupping_note>", views.cupping_note, name="cupping_note"),
    path("roast_level/<roast_level>", views.roast_level, name = "roast_level"),
    path("acidity/<acidity>", views.acidity, name="coffee_acidity"),
    path("processing/<processing>", views.processing, name="processing"),
]
