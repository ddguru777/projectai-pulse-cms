from django.contrib import admin
from .models import PageNav
from cms.models import Title

admin.site.site_header = 'ProjectAI Dashboard'

class PageNavAdmin(admin.ModelAdmin):
    def changelist_view(self, request, extra_context=None):
        published_cms_pages = Title.objects.filter(published=True, publisher_is_draft=False)
        unpublished_cms_pages = Title.objects.filter(published=False, publisher_is_draft=True)

        response = super(PageNavAdmin, self).changelist_view(request, extra_context)
        extra_context = {
            'published_pages_list': published_cms_pages,
            'unpublished_pages_list': unpublished_cms_pages
        }
        
        response.context_data.update(extra_context)
        
        return response

    change_list_template = 'admin/page_nav/page_nav_change_list.html'
    
admin.site.register(PageNav, PageNavAdmin)