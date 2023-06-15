from django.shortcuts import render
from .src.components.personalinfo import avatar
from backend.views import projectDetails, resourceDetails

def index(request):
    return render(request, "index.html", {"personal_info": avatar(), "projects": projectDetails(), "resources": resourceDetails()})