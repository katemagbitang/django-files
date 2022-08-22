from import_export import resources
from .models import fileRead

class FileReadResource(resources.ModelResource):
    class meta:
        model = fileRead