from django.contrib import admin
from django.urls import path, include
from .views import *

urlpatterns = [
    path("projects", projectDetails, name="projects"),
]