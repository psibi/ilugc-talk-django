from django.db import models

# Create your models here.
class post(models.Model):
    author = models.CharField(max_length = 30)
    title = models.CharField(max_length = 300)
    bodytext = models.TextField()
