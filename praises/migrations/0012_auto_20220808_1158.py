# Generated by Django 3.2.13 on 2022-08-08 15:58

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('praises', '0011_auto_20220728_2018'),
    ]

    operations = [
        migrations.AddField(
            model_name='praise',
            name='file',
            field=models.FileField(blank=True, null=True, upload_to='praises/pdf/', validators=[django.core.validators.FileExtensionValidator(['pdf'])]),
        ),
        migrations.AlterField(
            model_name='praise',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='praises/'),
        ),
    ]
