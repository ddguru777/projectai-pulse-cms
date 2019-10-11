from django.contrib import admin
from .models import AMQuestion, AMQuestionSHGroup, AMResponse, AMResponseTopic

# Register your models here.
admin.site.register(AMQuestion)
admin.site.register(AMQuestionSHGroup)
admin.site.register(AMResponse)
admin.site.register(AMResponseTopic)