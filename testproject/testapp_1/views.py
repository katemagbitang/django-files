from django.http import HttpResponse
from django.shortcuts import render

from .models import testModel

def index(request):
    return render(request,'index.html')   

def upload(request):
    testFiles = testModel.objects.all()
    return render(request,'uploaded.html', {
        'testFiles' : testFiles
    })