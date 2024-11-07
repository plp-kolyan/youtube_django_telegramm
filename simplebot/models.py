from django.db import models
import requests
from serveses_config import bot_token


# Create your models here.
class Answer(models.Model):
    command = models.CharField(max_length=10)
    text = models.TextField()

class SendMessage(models.Model):
    URL = ("https://api.telegram.org/bot"
           + bot_token
           + "/sendMessage")
    chat_id = models.CharField(max_length=25)
    text = models.TextField()

    def save(self, *args, **kwargs):
        requests.post(self.URL, data={
            "chat_id": self.chat_id,
            "text": self.text
        })
        return super().save(*args,
                            **kwargs)