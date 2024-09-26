from django.db import models
from cloudinary.uploader import upload

import cloudinary
import cloudinary.uploader
from cloudinary.utils import cloudinary_url
from cloudinary.models import CloudinaryField
from environ import Env
import os

env = Env()
Env.read_env()
ENVIRONMENT = env('ENVIRONMENT', default='producton')

cloudinary.config( 
    cloud_name = env('CLOUD_NAME'), 
    api_key = env('CLOUD_API_KEY'), 
    api_secret = env('CLOUD_API_SECRET'),
    secure=True
)

class Tag(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name


class Project(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(max_length=2000)
    notes = models.TextField(max_length=5000, blank=True)
    tags = models.ManyToManyField(Tag, related_name="projects", blank=True)
    link = models.URLField(max_length=200, blank=True)

    def __str__(self):
        return self.title


class ProjectImage(models.Model):
    project = models.ForeignKey(
        Project, related_name="images", on_delete=models.CASCADE
    )
    image = CloudinaryField('image', folder='project_images')  # Use CloudinaryField instead of FileField

    def __str__(self):
        return f"{self.project.title} Image"
