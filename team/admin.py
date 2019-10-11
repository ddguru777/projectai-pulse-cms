from django.contrib import admin
from .models import Team

class TeamAdmin(admin.ModelAdmin):
    # Exclude
    # exclude = ['name']

    # Order
    fields = ['name', 'organization']

    # Search
    search_fields = ['name', 'organization']

    # Filter
    list_filter = ['name', 'organization']

    # list
    list_display = ['name', 'organization']

    # Edit
    list_editable = ['organization']

    # Custom template
    # change_list_template = "admin/team/team_change_list.html"

# Register your models here.
admin.site.register(Team, TeamAdmin)