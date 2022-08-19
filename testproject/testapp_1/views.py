from django.http import HttpResponseRedirect
from django.shortcuts import render

from .models import testModel
from .forms import UploadFileForm

def index(request):
    # if request.method == 'POST':
    #     filled_form = UploadFileForm(request.POST)
    #     if filled_form.is_valid():
    #         note = 'Uploaded'
    #         new_form = UploadFileForm()
    #         return render(request,'index.html', {'uploadform':new_form, 'note':note})    
    # else:
    #     form = UploadFileForm()
    #     return render(request,'index.html', {'uploadform':form})

    form = UploadFileForm()
    return render(request,'index.html', {'uploadform':form})   