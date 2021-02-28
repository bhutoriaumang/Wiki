from django.urls import path

from . import views

app_name = "encyclopedia"

urlpatterns = [
    path("", views.index, name="index"),
    path("page",views.page, name="page"),
    path("create", views.create, name="create"),
    path("createpage", views.createpage, name="createpage"),
    path("random", views.random, name="random"),
    path("<str:entry>",views.entry, name="entry"),
]
