from django.db import models


class project(models.Model):
    name = models.CharField(max_length=255, default="")
    image = models.ImageField(upload_to="static/", default="")
    description = models.CharField(max_length=500, default="")
    link = models.CharField(max_length=2083, default="")
    category = models.CharField(max_length=50, default="")
    
