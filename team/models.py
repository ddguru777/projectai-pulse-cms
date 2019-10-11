from django.db import models
from organization.models import Organization

# Create your models here.
class Team(models.Model):
    organization = models.ForeignKey(Organization, on_delete=models.DO_NOTHING)
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

    