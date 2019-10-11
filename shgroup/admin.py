from django.contrib import admin
from .models import SHGroup, SHGroupUser, SHCategory, SHMapping

# Register your models here.
admin.site.register(SHGroup)
admin.site.register(SHGroupUser)
admin.site.register(SHCategory)
admin.site.register(SHMapping)