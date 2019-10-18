from django.contrib import admin
from .models import PageSetting, ExtendedPage
from aboutme.models import AMQuestion
from aboutothers.models import AOQuestion
from cms.admin.pageadmin import PageAdmin
from cms.models.pagemodel import Page
from jet.admin import CompactInline

class ExtendedPageAdmin(admin.StackedInline):
    model = ExtendedPage
    can_delete = False

PageAdmin.inlines.append(ExtendedPageAdmin)
try:
    admin.site.unregister(Page)
except:
    pass
admin.site.register(Page, PageAdmin)

class AMQuestionInline(CompactInline):
    model = AMQuestion
    extra = 0

class AOQuestionInline(CompactInline):
    model = AOQuestion
    extra = 0

class PageSettingAdmin(admin.ModelAdmin):
    #fields = ['page', 'pageType']
    fieldsets = [
        (None,      {'fields': ('page', 'pageType')}),
    ]

    inlines = [AMQuestionInline, AOQuestionInline]

    list_display = ('page', 'pageType')

admin.site.register(PageSetting, PageSettingAdmin)
