# Generated by Django 4.1 on 2022-08-26 07:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('testapp_1', '0003_alter_partoneimport_ishighpriority_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='partoneimport',
            name='isHighPriority',
            field=models.CharField(default='No', max_length=5),
        ),
        migrations.AlterField(
            model_name='partoneimport',
            name='security',
            field=models.CharField(default='Internal Use', max_length=20),
        ),
    ]