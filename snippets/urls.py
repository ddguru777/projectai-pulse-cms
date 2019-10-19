from django.conf.urls import include, url
from rest_framework.urlpatterns import format_suffix_patterns
from snippets import views

urlpatterns = [
    url('snippets/', views.SnippetList.as_view()),
    url('snippets/<int:pk>', views.SnippetDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)