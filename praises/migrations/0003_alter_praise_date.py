# Generated by Django 3.2.12 on 2022-06-03 00:00

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('praises', '0002_auto_20220602_2336'),
    ]

    operations = [
        migrations.AlterField(
            model_name='praise',
            name='date',
            field=models.DateField(default=django.utils.timezone.now),
        ),
    ]
