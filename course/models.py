from django.db import models

# Create your models here.


class Course(models.Model):
    semester_list = (
        ('Fall', 'Fall'),
        ('Summer', 'Summer'),
        ('Spring', 'Spring'),
    )
    course = models.TextField()
    subject = models.TextField()
    grade = models.TextField()
    location = models.CharField(max_length=50, blank=True)
    credit = models.IntegerField(default=3)
    instructor = models.CharField(max_length=30, blank=True)
    semester = models.CharField(max_length=6, choices=semester_list, blank=True)
    year = models.IntegerField(default=2022)
