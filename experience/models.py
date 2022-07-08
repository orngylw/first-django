from django.db import models

# Create your models here.

class Experience(models.Model):
    job = models.TextField()
    year = models.TextField()
    desc = models.TextField()