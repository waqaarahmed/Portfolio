from django.contrib import admin
from .models import project

class ProjectAdmin(admin.ModelAdmin):
    list_display = ('name', 'image')
    
    
admin.site.register(project, ProjectAdmin)
