from django.contrib.auth.models import User, Group
from page_setting.models import PageSetting
from rest_framework import viewsets
from mysite.quickstart.serializers import UserSerializer, GroupSerializer, PageSettingSerializer

class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by("-date_joined")
    serializer_class = UserSerializer

class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer

class PageSettingViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows page contents to be viewed or edited.
    """
    queryset = PageSetting.objects.all()
    serializer_class = PageSettingSerializer