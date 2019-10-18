from django.contrib.auth.models import User, Group
from page_setting.models import PageSetting
from rest_framework import serializers

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups']

class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['url', 'name']

class PageSettingSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = PageSetting
        fields = '__all__'