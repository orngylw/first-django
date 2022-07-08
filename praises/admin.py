from django.contrib import admin
from .models import Praise
# Register your models here.


class PraiseAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']
    search_fields = ['name', 'date']

admin.site.register(Praise, PraiseAdmin)