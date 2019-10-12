from django.db import models
from cms.models import Page

# Create your models here.
class PageNav(models.Model):
    page = models.OneToOneField(Page, on_delete=models.CASCADE, primary_key=True)
    order = models.PositiveIntegerField(unique=True)
