from django.contrib import admin
from simplebot.models import Answer


@admin.register(Answer)
class AnswerAdmin(admin.ModelAdmin):
    pass
# Register your models here.
