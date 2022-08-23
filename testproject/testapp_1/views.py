from django.http import HttpResponse
from django.shortcuts import render

from .models import fileRead, testModel
from .forms import UploadFileForm
from .resources import FileReadResource
from django.contrib import messages
from tablib import Dataset

def index(request):
    return render(request,'index.html')

# uploading to local directory
def upload(request):
    if request.method == 'POST':
        filled_form = UploadFileForm(request.POST, request.FILES)
        if filled_form.is_valid():
            note = 'Uploaded'
            # handle_uploaded_file(request.FILES['testFile'])
            model_instance = filled_form.save()
            model_instance.save()
            new_form = UploadFileForm()
            return render(request,'upload.html', {'uploadform':new_form, 'note':note})
            # return render(request,'index.html', {'uploadform':form})       
    else:
        form = UploadFileForm()
        return render(request,'upload.html', {'uploadform':form})

    # form = UploadFileForm()
    # return render(request,'index.html', {'uploadform':form})
    

def filesList(request):
    files = fileRead.objects.all()
    return render(request,'files_list.html',{
        'files':files
    })   

# Import excel file
def importFile(request):
    if request.method == 'POST':
        file_resource = FileReadResource()
        dataset = Dataset()
        new_file = request.FILES['myfile']

        if not new_file.name.endswith('xlsx'):
            # messages.info(request,'Wrong File Format')
            return render(request,'import.html',{'note':'Wrong File Format'})

        imported_data = dataset.load(new_file.read(),format='xlsx')
        for data in imported_data:
            value = fileRead(data[0],data[1],data[2],data[3],data[4],data[5],data[6],data[7],data[8],data[9],data[10],
                                data[11],data[12],data[13],data[14],data[15],data[16],data[17],data[18],data[19],data[20])
            value.save()
        return render(request, 'import.html',{'note':'Imported'})
    else:
        return render(request, 'import.html')