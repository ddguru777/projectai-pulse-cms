from django.contrib import admin, messages
from .models import PageNav
from cms.models import Title, Page
from django.http import HttpResponse, JsonResponse
import json

# admin.site.site_header = 'ProjectAI Dashboard'
# admin.site.site_title = 'ProjectAI Administration'
class PageNavAdmin(admin.ModelAdmin):
            
    def changelist_view(self, request, extra_context=None):
        # response
        published_cms_pages = PageNav.objects.filter(page__publisher_is_draft=False).order_by('order')
        unpublished_cms_pages = Title.objects.filter(publisher_is_draft=False)

        unordered_pages = []

        for item in unpublished_cms_pages:
            unordered_pages.append(item)

        for item in published_cms_pages:
            for item1 in unordered_pages:
                if item.page_id == item1.page_id:
                    unordered_pages.remove(item1)

        response = super(PageNavAdmin, self).changelist_view(request, extra_context)
        extra_context = {
            'published_pages_list': published_cms_pages,
            'unpublished_pages_list': unordered_pages
        }
        
        response.context_data.update(extra_context)
        
        return response

    def likePost(request):
        if request.method == 'POST':
            data = json.loads(request.POST.get('data', ''))

            PageNav.objects.filter().delete()

            for item in data:
                order = PageNav(order=item['order'], page_id=item['id'])
                order.save()
                Title.objects.filter(pk=item['id']).update(published=True)
                
            messages.success(request, 'The page order was saved successfully.')
            return JsonResponse('Success', safe=False)
        else:
            messages.error(request, 'Save request failed.')
            return JsonResponse('Failed', safe=False)

    change_list_template = 'admin/page_nav/page_nav_change_list.html'

admin.site.register(PageNav, PageNavAdmin)
