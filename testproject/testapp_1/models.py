from django.db import models

# Create your models here.
class testModel(models.Model):
    requestor = models.CharField(max_length=50)
    testFile = models.FileField()