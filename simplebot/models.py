from django.db import models

# Create your models here.
class Answer(models.Model):
    command = models.CharField(max_length=10)
    text = models.TextField()