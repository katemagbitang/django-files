from django.http import HttpResponseRedirect
from django.shortcuts import render

from .models import testModel
from .forms import UploadFileForm
from .functions import handle_uploaded_file

def index(request):
    if request.method == 'POST':
        filled_form = UploadFileForm(request.POST, request.FILES)
        if filled_form.is_valid():
            note = 'Uploaded'
            handle_uploaded_file(request.FILES['testFile'])
            model_instance = filled_form.save()
            model_instance.save()
            new_form = UploadFileForm()
            return render(request,'index.html', {'uploadform':new_form, 'note':note})
            # return render(request,'index.html', {'uploadform':form})       
    else:
        form = UploadFileForm()
        return render(request,'index.html', {'uploadform':form})

    # form = UploadFileForm()
    # return render(request,'index.html', {'uploadform':form})   