from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.models import Permission
from team.models import Team
from survey.models import Project
from shgroup.models import SHGroup

# Create your models here.
class ProjectUser(models.Model):
    project = models.ForeignKey(Project, on_delete=models.DO_NOTHING)
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    userPermission = models.ForeignKey(Permission, on_delete=models.DO_NOTHING)
    team = models.ForeignKey(Team, on_delete=models.DO_NOTHING)
    shGroup = models.ForeignKey(SHGroup, on_delete=models.DO_NOTHING)

