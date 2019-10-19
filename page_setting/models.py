from django.db import models
from cms.models.pagemodel import Page
from enumfields import EnumField
from enumfields import Enum

class PageType(Enum):
    PG_WELCOME1 = 0
    PG_WELCOME2 = 1
    PG_ABOUT_ME = 2
    PG_SURVEY = 3
    PG_NEW_STAKEHOLDER = 4
    PG_ABOUT_STAKEHOLDER = 5
    PG_RESULT = 6
    
    class Labels:
        PG_WELCOME1 = 'Welcome 1'
        PG_WELCOME2 = 'Welcome 2'
        PG_ABOUT_ME = 'About Me'
        PG_SURVEY = 'Survey'
        PG_NEW_STAKEHOLDER = 'New StakeHolder'
        PG_ABOUT_STAKEHOLDER = 'About StakeHolder'
        PG_RESULT = 'Result'

class PageSetting(models.Model):
    page = models.OneToOneField(Page, related_name='pages', on_delete=models.CASCADE, primary_key=True)
    pageType = EnumField(PageType, max_length=1)

class ExtendedPage(models.Model):
    page = models.OneToOneField(Page, verbose_name="Page", editable=False, related_name='extended_fields')
    my_extra_field = models.CharField(max_length=50)