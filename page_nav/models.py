from django.db import models

# Create your models here.
class PageNav(models.Model):
    order = models.PositiveIntegerField()
