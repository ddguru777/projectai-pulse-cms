from django.db import models
from survey.models import Survey, Driver
from setting.models import ControlType
from shgroup.models import SHGroup
from page_setting.models import PageSetting
from django.contrib.auth.models import User

# Create your models here.
class AMQuestion(models.Model):
    survey = models.ForeignKey(Survey, on_delete=models.DO_NOTHING)
    driver = models.ForeignKey(Driver, on_delete=models.DO_NOTHING)
    subdriver = models.CharField(max_length=50)
    questionText = models.CharField(max_length=1000)
    controlType = models.ForeignKey(ControlType, on_delete=models.DO_NOTHING)
    sliderTextLeft = models.CharField(max_length=50)
    sliderTextRight = models.CharField(max_length=50)
    skipOptionYN = models.BooleanField(default=True)
    skipResponses = models.CharField(max_length=1000)
    questionSequence = models.PositiveIntegerField()
    topicPrompt = models.CharField(max_length=255)
    commentPrompt = models.CharField(max_length=255)
    PageSetting = models.ForeignKey(PageSetting, related_name="ampagesetting", on_delete=models.SET_NULL, default=None, blank=True, null=True)

    def __str__(self):
        return self.questionText

class AMQuestionSHGroup(models.Model):
    amQuestion = models.ForeignKey(AMQuestion, on_delete=models.DO_NOTHING)
    shGroup = models.ForeignKey(SHGroup, on_delete=models.DO_NOTHING)

class AMResponse(models.Model):
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING, related_name="amUser")
    subjectUser = models.ForeignKey(User, on_delete=models.DO_NOTHING, related_name="amSubjectUser")
    survey = models.ForeignKey(Survey, on_delete=models.DO_NOTHING)
    amQuestion = models.ForeignKey(AMQuestion, on_delete=models.DO_NOTHING)
    integerValue = models.PositiveIntegerField()
    topicValue = models.TextField()
    commentValue = models.TextField()
    skipValue = models.TextField()
    topicTags = models.TextField()
    commentTags = models.TextField()

class AMResponseTopic(models.Model):
    amResponse = models.ForeignKey(AMResponse, on_delete=models.DO_NOTHING)
    topic = models.CharField(max_length=100)
    comment = models.CharField(max_length=1000)