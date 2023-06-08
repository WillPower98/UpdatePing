from django.contrib import admin
from django.urls import include, path
from . import views

urlpatterns = [
    #ex: /update-ping/
    path("", views.index, name="index")
]