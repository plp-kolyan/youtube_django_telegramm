from django.contrib import admin
from simplebot.models import Answer, SendMessage


@admin.register(Answer)
class AnswerAdmin(admin.ModelAdmin):
    pass
# Register your models here.

@admin.register(SendMessage)
class SendMessageAdmin(admin.ModelAdmin):
    pass