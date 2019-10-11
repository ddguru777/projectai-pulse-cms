from django.db import models
from survey.models import Project, Survey
from django.contrib.auth.models import User
# If you use a custom user model you should use:
# from django.contrib.auth import get_user_model
# User = get_user_model()
from organization.models import Organization

# Create your models here.
class SHGroup(models.Model):
    SHGroupName = models.CharField(max_length=255)
    SHGroupAbbrev = models.CharField(max_length=50)
    project = models.ForeignKey(Project, on_delete=models.DO_NOTHING)

    def __str__(self):
        return self.SHGroupName

class SHGroupUser(models.Model):
    shGroup = models.ForeignKey(SHGroup, on_delete=models.DO_NOTHING)
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING)

class SHCategory(models.Model):
    survey = models.ForeignKey(Survey, on_delete=models.DO_NOTHING)
    shGroup = models.ForeignKey(SHGroup, on_delete=models.DO_NOTHING)
    mapType = models.CharField(max_length=50)
    colour = models.CharField(max_length=50)
    icon = models.CharField(max_length=100)
    SHCategoryName = models.CharField(max_length=50)
    SHCategoryDesc = models.CharField(max_length=200)

    def __str__(self):
        return self.SHCategoryName

class SHMapping(models.Model):
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING, related_name="user")
    subjectUser = models.ForeignKey(User, on_delete=models.DO_NOTHING, related_name="subjectUser")
    organization = models.ForeignKey(Organization, on_delete=models.DO_NOTHING)
    shCategory = models.ForeignKey(SHCategory, on_delete=models.DO_NOTHING)
    relationshipStatus = models.CharField(max_length=100)