from django.contrib import admin
from django.urls import include, path
from . import views

urlpatterns = [
    path("update-ping/", include("updateping.urls")),
    path("admin/", admin.site.urls),

    # ex: /update-ping/
    path("", views.index, name="index"),

    # ex: /update-ping/user_games
    path("<int:user_id>/games". views.games, name="user_games")
]