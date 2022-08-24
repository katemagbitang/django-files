import re

def handle_uploaded_file(f):
    with open('testapp_1/files' + f.name, 'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)

def validateEmail(email):
    regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
    if(re.fullmatch(regex, email)):
        return email
    else:
        return 'Invalid Email'

# def numberToString(f):
#     f = str(f)
#     return f

# def nullToBlank(f):
#     if f == ''