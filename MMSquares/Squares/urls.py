from os import name
from django.urls import path
from . import views


urlpatterns = [
    path("", views.homepage, name="homepage"),
    path("logout_user", views.logout_user, name="logout_user"),
    path("login_user", views.login_user, name="login_user"),
    path("upload", views.upload, name="upload"),
    path("how-to-play", views.directions, name="directions"),
    path("quick-settings", views.quick_settings, name="quick_settings")
]