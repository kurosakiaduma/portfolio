from django.shortcuts import render
from .components import PersonalInfo
from backend.views import projectDetails, resourceDetails

def index(request):
    projects = projectDetails()
    resources = resourceDetails()
    return render(request, "index.html", {"personal_info": PersonalInfo(), "projects": projects, "resources": resources})