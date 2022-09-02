# [R&D] Excel Import for Requests

This repository is currently being used to study the Excel Bulk Upload/Import using Python-Django.

## Setup

The first thing to do is to clone the repository:

```sh
$ git clone https://github.com/katemagbitang/django-files.git
$ cd django-files
```
Then install the dependencies:

```sh
$ pip install
```
Once `pip` has finished downloading the dependencies:

```sh
$ cd testproject
$ python manage.py runserver
```
And navigate to `http://127.0.0.1:8000/`.

## Walkthrough

Upon landing on `http://127.0.0.1:8000/`, there will be a simple navigation bar, with buttons, `Home`, `Import Excel`, and `Imported Data`. The buttons navigate to the following:

- `Home` is the landing page (which is empty as of the moment)
- `Import Excel` is the page where a user can upload an Excel file to import the data
- `Imported Data` is where the imported data will be reflected.

The 'Import Excel' file upload will only accept an Excel file. Also, for the file to be imported properly, the table below is how the columns should be labelled as such on Row `1`:

| Column | Field                        |
|--------|------------------------------|
| A      |  id                          |
| B      |  userID                      |
| C      |  isHighPriority              |
| D      |  materialDescription         |
| E      |  unitOfMeasurement           |
| F      |  materialGroup               |
| G      |  manufacturerName            |
| H      |  materialPartNumber          |
| I      |  attachment                  |
| J      |  isDocumented                |
| K      |  ibauNum                     |
| L      |  ibauName                    |
| M      |  functionalLocations         |
| N      |  vendorName                  |
| O      |  vendorPartNum               |
| P      |  vendorPartNumRevision       |
| Q      |  technicalContact            |
| R      |  security                    |
| S      |  tcProjectId                 |

The following fields are **required** to have an input under the field:
- materialDescription 
- unitOfMeasurement
- materialGroup
- manufacturerName
- materialPartNumber
- attachment
- isDocumented
- functionalLocations
- security
- tcProjectId

`attachment` currently accepts a string input in the meantime.

For more information about the fields, kindly check the **Data Dictionary - Request** on Confluence.

Once an Excel file has been imported, the data placed on the second row of the Excel file will reflect on the table.

## Admin
Admin documentation is to be followed.
