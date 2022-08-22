from asyncio.windows_events import NULL
from unittest.util import _MAX_LENGTH
from django.db import models

# Create your models here.
class testModel(models.Model):
    requestor = models.CharField(max_length=50)
    testFile = models.FileField(upload_to='files/', null=True, verbose_name="")

    def __str__(self):
        return self.requestor + ': ' + str(self.testFile)

class fileRead(models.Model):
    requestorName = models.CharField(max_length=100, null=False)
    requestorEmail = models.EmailField(null=False)
    requestorTNum = models.CharField(max_length=30, null=False)
    businessUnit = models.CharField(max_length=100, null=False) # picklist
    plantCode = models.CharField(max_length=100, null=False) # picklist
    requestName = models.CharField(max_length=100, null=False)
    projectManager = models.CharField(max_length=100, null=True)
    sapCode = models.CharField(max_length=30, null=True)
    userID = models.CharField(max_length=100, null=True)
    isHighPriority = models.BooleanField(default=False)
    materialDescription = models.CharField(max_length=40, null=False)
    unitOfMeasurement = models.CharField(max_length=5, null=False) # picklist
    materialGroup = models.CharField(max_length=100, null=False) # picklist
    manufacturerName = models.CharField(max_length=100, null=False)
    materialPartNumber = models.CharField(max_length=100, null=False)
    attachment = models.CharField(max_length=100, null=False) # replace to file field once model is established
    isDocumented = models.BooleanField(default=False)
    ibauNum = models.CharField(max_length=30, null=True)
    ibauName = models.CharField(max_length=100, null=True)
    functionalLocations = models.CharField(max_length=30, null=False)