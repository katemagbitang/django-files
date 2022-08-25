from import_export import resources
from .models import fileRead, partOneImport

class FileReadResource(resources.ModelResource):
    class meta:
        model = fileRead

class PartOneReadResource(resources.ModelResource):
    class meta:
        model = partOneImport