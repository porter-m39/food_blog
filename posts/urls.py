# posts/urls.py

from django.urls import path
from . import views

app_name = 'posts' #this designates that the names of the URLs below belong to the posts app. So in the html files, write posts:<name>

urlpatterns = [
    path("", views.post_index,name="post_index"),
    path("tag/<tag>/",views.post_tag,name="post_tag"),
    path('<slug:slug>',views.post_detail,name="post_detail"),
]
