from django.db import models
from survey.models import Survey, Driver
from setting.models import ControlType
from shgroup.models import SHGroup
from page_setting.models import PageSetting
from django.contrib.auth.models import User

# Create your models here.
class AOQuestion(models.Model):
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
    PageSetting = models.ForeignKey(PageSetting, on_delete=models.SET_NULL, related_name="aopagesetting", default=None, blank=True, null=True)
    
    def __str__(self):
        return self.questionText

class AOQuestionSHGroup(models.Model):
    aoQuestion = models.ForeignKey(AOQuestion, on_delete=models.DO_NOTHING)
    shGroup = models.ForeignKey(SHGroup, on_delete=models.DO_NOTHING)

class AOResponse(models.Model):
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING, related_name="aoUser")
    subjectUser = models.ForeignKey(User, on_delete=models.DO_NOTHING, related_name="aoSubjectUser")
    survey = models.ForeignKey(Survey, on_delete=models.DO_NOTHING)
    aoQuestion = models.ForeignKey(AOQuestion, on_delete=models.DO_NOTHING)
    integerValue = models.PositiveIntegerField()
    topicValue = models.TextField()
    commentValue = models.TextField()
    skipValue = models.TextField()
    topicTags = models.TextField()
    commentTags = models.TextField()

class AOResponseTopic(models.Model):
    aoResponse = models.ForeignKey(AOResponse, on_delete=models.DO_NOTHING)
    topic = models.CharField(max_length=100)
    comment = models.CharField(max_length=1000)

class AOPage(models.Model):
    aoPageName = models.CharField(max_length=50)
    aoPageSequence = models.PositiveIntegerField()

    def __str__(self):
        return self.aoPageName