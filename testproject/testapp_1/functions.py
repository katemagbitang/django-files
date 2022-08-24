import re

def handle_uploaded_file(f):
    with open('testapp_1/files' + f.name, 'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)

# checks if the email is valid
def validateEmail(email):
    regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
    if(re.fullmatch(regex, email)):
        return email
    else:
        return 'Invalid Email'

# checks if the business unit is part of P&G
def validateBusinessUnit(businessUnit):
    units = list(map(str.lower,['Baby Care', 'Fabric Care', 'Family Care', 'Feminine Care', 'Hair Care', 'Home Care', 'Oral Care', 'Personal Health Care', 'Shave Care', 'Skin and Personal Cleansing', 'Beauty Care', 'Global Business Services']))
    # print(units)
    businessUnit = str.lower(businessUnit)
    # print(businessUnit)
    for unit in units:
        # print(unit)
        if businessUnit == unit:
            return str.title(unit)
        else:
            unit = 'Unknown'
           
    return unit

# for tracing purposes
def readBusinessUnit():
    units = list(map(str.lower,['Baby Care', 'Fabric Care', 'Family Care', 'Feminine Care', 'Hair Care', 'Home Care', 'Oral Care', 'Personal Health Care', 'Shave Care', 'Skin and Personal Cleansing', 'Beauty Care', 'Global Business Services']))
    # print(units)
    # businessUnit = str.lower(businessUnit)
    # print(businessUnit)
    for unit in units:
        print(unit)
        # if businessUnit != unit:
        #     return 'Unknown Business Unit'
        # else:
        #     businessUnit = str.upper(businessUnit)


# def nullToBlank(f):
#     if f == ''