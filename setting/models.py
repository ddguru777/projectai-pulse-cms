from django.db import models

# Create your models here.
class ControlType(models.Model):
    controlTypeName = models.CharField(max_length=50)

    def __str__(self):
        return self.controlTypeName

class ConceptClass(models.Model):
    conceptClassName = models.CharField(max_length=50)
    childOf = models.PositiveIntegerField()
    conceptClassDesc = models.TextField()
    conceptClassIRI = models.TextField()

    def __str__(self):
        return self.conceptClassName

class ConceptInstance(models.Model):
    instanceName = models.CharField(max_length=100)
    conceptClass = models.ForeignKey(ConceptClass, on_delete=models.DO_NOTHING)
    instanceIRI = models.TextField()
    instanceDesc = models.TextField()

    def __str__(self):
        return self.instanceName