from django.db import models

# Create your models here.
class testModel(models.Model):
    uploader = models.CharField(max_length=50)
    testFile = models.FileField()