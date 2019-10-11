from django.contrib import admin
from .models import AOQuestion, AOQuestionSHGroup, AOResponse, AOResponseTopic, AOPage

# Register your models here.
admin.site.register(AOQuestion)
admin.site.register(AOQuestionSHGroup)
admin.site.register(AOResponse)
admin.site.register(AOResponseTopic)
admin.site.register(AOPage)