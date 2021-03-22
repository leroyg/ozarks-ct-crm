from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name="dashboard"),
    path('sports', views.sports, name="teams"),
    path('trainer', views.trainer, name="trainer"),
    path('team', views.team, name="team"),
    ]