# posts/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path("", views.post_index,name="post_index"),
    path("tag/<tag>/",views.post_tag,name="post_tag"),
    path('<slug:slug>',views.post_detail,name="post_detail"),
]
