from django.db import models

# from shgroup.models import SHGroup

class Client(models.Model):
    clientName = models.CharField(max_length=200)

    def __str__(self):
        return self.clientName

class Project(models.Model):
    client = models.ForeignKey(Client, on_delete=models.DO_NOTHING)
    projectName = models.CharField(max_length=200)

    def __str__(self):
        return self.projectName

class Survey(models.Model):
    project = models.ForeignKey(Project, on_delete=models.DO_NOTHING)
    surveyTitle = models.CharField(max_length=200)

    def __str__(self):
        return self.surveyTitle

class Driver(models.Model):
    driverName = models.CharField(max_length=200)

    def __str__(self):
        return self.driverName

