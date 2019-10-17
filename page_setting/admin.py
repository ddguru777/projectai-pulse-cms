from django.contrib import admin
from .models import PageSetting
from aboutme.models import AMQuestion
from aboutothers.models import AOQuestion

class AMQuestionInline(admin.StackedInline):
    model = AMQuestion
    extra = 0

class AOQuestionInline(admin.StackedInline):
    model = AOQuestion
    extra = 0

class PageSettingAdmin(admin.ModelAdmin):
    #fields = ['page', 'pageType']
    fieldsets = [
        (None,      {'fields': ['page', 'pageType']}),
    ]
    inlines = [AMQuestionInline, AOQuestionInline]

admin.site.register(PageSetting, PageSettingAdmin)
