from django.db import models
from django.utils import timezone

import datetime

# Create your models here.


class Praise(models.Model):
    chord_list=(
        ('C', 'C'),
        ('D', 'D'),
        ('Eb', 'Eb'),
        ('E', 'E'),
        ('F', 'F'),
        ('G', 'G'),
        ('A', 'A'),
        ('Bb', 'Bb'),
        ('B', 'B'),
    )
    name = models.TextField()
    img_path = models.TextField(blank=True)
    instruments = models.TextField(blank=True)
    chord = models.CharField(max_length=3, choices=chord_list, blank=True)
    key_up = models.TextField(max_length=3, default="X")
    date = models.DateField(default=timezone.now)
    note = models.CharField(max_length=256, blank=True)