from django.contrib import admin
from import_export.admin import ImportExportModelAdmin

# Register your models here.
from .models import testModel, fileRead

admin.site.register(testModel)

@admin.register(fileRead)
class FileReadAdmin(ImportExportModelAdmin):
    list_display = ('requestorName', 'requestorEmail', 'requestorTNum', 'businessUnit', 'plantCode', 'requestName', 'projectManager','sapCode', 'userID', 'isHighPriority', 'materialDescription', 'unitOfMeasurement', 'materialGroup', 'manufacturerName', 'materialPartNumber', 'attachment', 'isDocumented', 'ibauNum' ,'ibauName', 'functionalLocations' )