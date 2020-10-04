from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="time_index")
]

