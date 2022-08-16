from django.db import models
from django.utils import timezone
from django.core.validators import FileExtensionValidator
from django.core.exceptions import ValidationError
from django.urls import reverse

from tags.models import Tag

import datetime


class Praise(models.Model):
    def validate_file(self):
        filesize = self.file.size
        megabyte_limit = 5.0
        if filesize > megabyte_limit * 1024 * 1024:
            raise ValidationError("Max file size is %sMB" % str(megabyte_limit))

    chord_list = (
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
    instruments = models.TextField(blank=True)
    chord = models.CharField(max_length=3, choices=chord_list, blank=True)
    key_up = models.TextField(max_length=3, default="X")
    date = models.DateField(default=timezone.now)
    note = models.CharField(max_length=256, blank=True)
    image = models.ImageField(upload_to='praises/', blank=True, null=True, validators=[validate_file])
    file = models.FileField(upload_to='praises/pdf/', blank=True, null=True,
                            validators=[FileExtensionValidator(['pdf']), validate_file],)
    tags = models.ManyToManyField(to=Tag)

    def print_file_name(self):
        return self.file.name.split("/")[-1]

    def get_absolute_url(self):
        return reverse('praises:detail', kwargs={"id": self.id})
