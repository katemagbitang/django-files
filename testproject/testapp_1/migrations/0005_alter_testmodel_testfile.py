# Generated by Django 4.1 on 2022-08-22 02:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('testapp_1', '0004_delete_filemodel_testmodel_requestor'),
    ]

    operations = [
        migrations.AlterField(
            model_name='testmodel',
            name='testFile',
            field=models.FileField(null=True, upload_to='files/', verbose_name=''),
        ),
    ]
