from django.contrib import admin
from .models import ControlType, ConceptClass, ConceptInstance

# Register your models here.
admin.site.register(ControlType)
admin.site.register(ConceptClass)
admin.site.register(ConceptInstance)