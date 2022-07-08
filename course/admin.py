from django.contrib import admin
from .models import Course

# Register your models here.

class CourseAdmin(admin.ModelAdmin):
    list_display = ['id', 'subject']
    search_fields = ['subject', 'course']

admin.site.register(Course, CourseAdmin)