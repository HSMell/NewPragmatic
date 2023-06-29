from django.db import models

# Create your models here.

# class하나가 item 한개
class HelloWorld(models.Model):
    text = models.CharField(max_length=255, null=False)