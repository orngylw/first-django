# Generated by Django 3.2.13 on 2022-08-09 23:58

import django.core.validators
from django.db import migrations, models
import praises.models


class Migration(migrations.Migration):

    dependencies = [
        ('praises', '0012_auto_20220808_1158'),
    ]

    operations = [
        migrations.AlterField(
            model_name='praise',
            name='file',
            field=models.FileField(blank=True, null=True, upload_to='praises/pdf/', validators=[django.core.validators.FileExtensionValidator(['pdf']), praises.models.Praise.validate_file]),
        ),
        migrations.AlterField(
            model_name='praise',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='praises/', validators=[praises.models.Praise.validate_file]),
        ),
    ]
