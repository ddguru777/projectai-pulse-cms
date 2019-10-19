from django.conf.urls import include, url
from snippets import views

urlpatterns = [
    url('snippets/', views.snippet_list),
    url('snippets/<int:pk>/', views.snippet_detail),
]