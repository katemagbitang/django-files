# Generated by Django 4.1 on 2022-08-26 06:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('testapp_1', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='partoneimport',
            name='isHighPriority',
            field=models.CharField(max_length=30),
        ),
    ]