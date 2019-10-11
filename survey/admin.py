from django.contrib import admin
from .models import Survey, Client, Project, Driver

# Register your models here.
admin.site.register(Survey)
admin.site.register(Client)
admin.site.register(Project)
admin.site.register(Driver)