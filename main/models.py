from django.db import models
from cloudinary.uploader import upload

import cloudinary
import cloudinary.uploader
from cloudinary.utils import cloudinary_url

cloudinary.config( 
    cloud_name = "da9mmlfmi", 
    api_key = "827811635615798", 
    api_secret = "YBDgIcPfN9xEmRCf65LI3YYZ3nw",
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
    image = models.FileField(upload_to="project_images/")

    def __str__(self):
        return f"{self.project.title} Image"
