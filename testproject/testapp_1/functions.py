import re

def handle_uploaded_file(f):
    with open('testapp_1/files' + f.name, 'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)

# checks if the email is valid
# reference: https://www.geeksforgeeks.org/check-if-email-address-valid-or-not-in-python/
def validateEmail(email):
    regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
    if(re.fullmatch(regex, email)):
        return email
    else:
        return 'Invalid Email'

# checks if the business unit is part of P&G
def validateBusinessUnit(businessUnit):
    units = list(map(str.title,['Baby Care', 'Fabric Care', 'Family Care', 'Feminine Care', 'Hair Care', 'Home Care', 'Oral Care', 'Personal Health Care', 'Shave Care', 'Skin and Personal Cleansing', 'Beauty Care', 'Global Business Services']))
    # print(units)
    
    businessUnit = str.title(businessUnit)
    # print(businessUnit)
    for unit in units:
        # print(unit)
        if businessUnit == unit:
            return unit
        else:
            unit = 'Unknown'
           
    return unit

def validatePlant(plantCode):
    plants = list(map(str.upper,['1702 LIMA-OHIO-PLANT', '1719 GREENSBORO SWING ROAD PLANT',
                                '1725 PHOENIX PLANT', '1727 ALEXANDRIA PLANT','2475 AMIENS PLANT - TOLL MFG',
                                '3352 SHANGHAI M&S PLANT-GILLETTE','423 BEN CAT-PLANT-M&S-P&G INDO LTD','4526 READING PLANT-GILLETTE UK LTD',
                                '4559 BADDI PLANT-M&S-GILLETTE INDIA','4769 TAKASAKI PLANT-TOLL','8257 BHIWADI TS PLANT - GIL','8323 ANDOVER PLANT-GILLETTE CO',
                                '8333 BOSTON PLANT-GILLETTE CO','8335 IOWA CITY PLANT-ORAL B LABS','9245 MANAUS M&S PLANT-PG DO BR','9617 BERLIN PLANT-GILLETTE GMBH',
                                '9797 BIN DUONG-PLT-MS-PG INDOCHINA','9891 LODZ-PLANT-GILL POLAND INTERL','9902 ST. PETERSBURG PLANT-PPI','B680 TABLER STATION','B710 VALLEJO -MFG- PG SERV TECN',
                                'B713 MILENIO -MFG- PG SERV TECN','B716 NAUCALPAN -MFG- PG SERV TECN','C490 AHMEDABAD-TS-GIL DVRSFD OPS','C527 P&G HEALTH AUSTRIA GMBH & CO. OG',
                                'C600 GOA-MFG-MERCK LTD','C602 SPITTAL','A993 RIO NEGRO PLANT']))

    plantCode = str.upper(plantCode)
    for plant in plants:
        # when the field only has the plant code on the excel
        if len(plantCode) == 4:
            for plant in plants:
                x = plant.split(' ',1)
                # print(x)
                if x[0] == plantCode:
                    return plant
                else:
                    plant = 'No such plant'
        # elif if the field only placed the plant name to follow if needed           
        elif plantCode == plant:
            return plant
        else:
            plant = 'No such plant'
    
    return plant

# temporary; will fill in empty fields
def checkEmptyFields(field):
# fields that are mandatory:
# businessUnit data[4]
# plantCode data[5]
# requestName data[6]
# materialDescription data[11]
# unitOfMeasurement data[12]
# materialGroup data[13]
# manufacturerName data[14]
# materialPartNumber data[15]
# attachment data[16]
# functionalLocations data[20]
    if field == None:
        field = 'To be filled manually'
    return field

def validateMeasureUnit(unitOfMeasurement):
    units = list(map(str.title,['EA (Each)', 'KG (Kilogram)',
                                'L (Liter)', 'M (Meter)','M2 (Square Meter)',
                                'PR (Pair)']))

    unitOfMeasurement = str.title(unitOfMeasurement)
    for unit in units:
        # when the field only has the acronym of the unit on the excel
        if len(unitOfMeasurement) < 3:
            for unit in units:
                x = unit.split(' ',1)
                # print(x)
                if x[0] == unitOfMeasurement:
                    return unit
                else:
                    unit = 'No such unit'
        # elif if the field only placed the plant name to follow if needed           
        elif unitOfMeasurement == unit:
            return unit
        else:
            unit = 'No such unit'
    
    return unit

def validateMaterialGrp(materiaGroup):
    groups = list(map(str.title,['OEM-G40150000', 'Commercial-G310000AA',
                                'Fabricated-G31000000']))

    materiaGroup = str.title(materiaGroup)
    for group in groups:
        # when the field only has the 9-digits OR the group name on the excel
        if len(materiaGroup) < 10:
            for group in groups:
                x = group.split('-',1)
                # print(x)
                if x[1] == materiaGroup:
                    return group
                elif x[0] == materiaGroup: # not working: getting name
                    return group
                else:
                    group = 'No such group'
        elif materiaGroup == group:
            return group
        else:
            group = 'No such group'
    
    return group