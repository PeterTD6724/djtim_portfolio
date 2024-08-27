from django.shortcuts import render, get_object_or_404
from .models import Project, Tag
import cloudinary
import cloudinary.api
import cloudinary.uploader
from environ import Env
import environ

env = Env()
ENVIRONMENT = env('ENVIRONMENT', default='producton')

env = environ.Env()
environ.Env.read_env() 

cloudinary.config(
    cloud_name="da9mmlfmi",
    api_key="827811635615798",
    api_secret="CLOUD_API_SECRET",
    secure=True,
)

def home(request):
    projects = Project.objects.all()
    tags = Tag.objects.all()
    return render(request, "home.html", {"projects": projects, "tags": tags})


def contact(request):
    return render(request, "contact.html")


def project(request, id):
    project = get_object_or_404(Project, pk=id)
    return render(request, "project.html", {"project": project})

