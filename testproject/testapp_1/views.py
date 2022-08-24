from django.http import HttpResponse
from django.shortcuts import render

from .models import fileRead, testModel
from .forms import UploadFileForm
from .resources import FileReadResource
from tablib import Dataset
from .functions import validateEmail, validateBusinessUnit, validatePlant, checkEmptyFields, validateMeasureUnit, validateMaterialGrp

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

        # for tracing purposes
        # readBusinessUnit()

        imported_data = dataset.load(new_file.read(),format='xlsx')
        # intial loop
        # 
        # for data in imported_data:
        #     value = fileRead(data[0],data[1],data[2],data[3],data[4],data[5],data[6],data[7],data[8],data[9],data[10],
        #                         data[11],data[12],data[13],data[14],data[15],data[16],data[17],data[18],data[19],data[20])
        #     value.save()
        for data in imported_data:

            mandatory_fields = [data[4],data[5],data[6],data[11],data[12],data[13],data[14],data[15],data[16],data[20]]
            
            # check if the mandatory fields are empty to be replaced with another string
            isFilledBU = checkEmptyFields(data[4])
            isFilledPlant = checkEmptyFields(data[5])
            isFilledReqName = checkEmptyFields(data[6])
            isFilledMatDes = checkEmptyFields(data[11])
            isFilledMeasureUnit = checkEmptyFields(data[12])
            isFilledMatGroup = checkEmptyFields(data[13])
            isFilledManuName = checkEmptyFields(data[14])
            isFilledPartNum = checkEmptyFields(data[15])
            isFilledAttach = checkEmptyFields(data[16]) # url or file path soon
            isFilledLocation = checkEmptyFields(data[20])
            
            # checks if the email is valid
            validatedEmail = validateEmail(data[2])
            # print(validatedEmail)

            # checks if the business unit is part of P&G
            validatedBU = validateBusinessUnit(isFilledBU)
            # print(validatedBU)

            # checks if the plant code and name is part of P&G
            validatedPlant = validatePlant(isFilledPlant)
            # print(validatedPlant)

            # checks if the unit of measurement is valid
            validatedMeasureUnit = validateMeasureUnit(isFilledMeasureUnit)
            # print(validatedPlant)

            # checks if the material group is valid
            validatedMatGrp = validateMaterialGrp(isFilledMatGroup);
        
            value = fileRead(data[0],data[1],validatedEmail,data[3],validatedBU,validatedPlant,isFilledReqName,data[7],data[8],data[9],data[10],
                                isFilledMatDes,validatedMeasureUnit,validatedMatGrp,isFilledManuName,isFilledPartNum,isFilledAttach,data[17],data[18],data[19],isFilledLocation)
            value.save()
        return render(request, 'import.html',{'note':'Imported'})
    else:
        return render(request, 'import.html')