from django.contrib import admin

# Register your models here.
from .models import testModel

admin.site.register(testModel)