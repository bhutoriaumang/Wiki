from django.urls import path

from . import views

app_name = "encyclopedia"

urlpatterns = [
    path("", views.index, name="index"),
    path("page",views.page, name="page"),
    path("<str:entry>/",views.entry, name="entry")
]
