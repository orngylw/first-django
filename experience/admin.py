from django.contrib import admin

from .models import Experience
# Register your models here.

class ExpAdmin(admin.ModelAdmin):
    list_display = ['id', 'job']
    search_fields = ['job', 'year']

admin.site.register(Experience, ExpAdmin)