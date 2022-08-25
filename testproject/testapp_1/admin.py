from django.contrib import admin
from import_export.admin import ImportExportModelAdmin

# Register your models here.
from .models import testModel, fileRead, partOneImport

admin.site.register(testModel)

@admin.register(fileRead)
class FileReadAdmin(ImportExportModelAdmin):
    list_display = ('requestorName', 'requestorEmail', 'requestorTNum', 'businessUnit', 'plantCode', 'requestName', 'projectManager','sapCode', 'userID', 'isHighPriority', 'materialDescription', 'unitOfMeasurement', 'materialGroup', 'manufacturerName', 'materialPartNumber', 'attachment', 'isDocumented', 'ibauNum' ,'ibauName', 'functionalLocations' )

@admin.register(partOneImport)
class FileReadAdmin(ImportExportModelAdmin):
    list_display = ('userID', 'isHighPriority', 'materialDescription', 'unitOfMeasurement', 'materialGroup', 'manufacturerName', 'materialPartNumber', 'attachment', 'isDocumented', 'ibauNum' ,'ibauName', 'functionalLocations','vendorName', 'vendorPartNum', 'vendorPartNumRevision', 'technicalContact', 'security', 'tcProjectId' )