# Generated by Django 3.2.12 on 2022-06-06 17:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='credit',
            field=models.IntegerField(default=3),
        ),
        migrations.AddField(
            model_name='course',
            name='location',
            field=models.CharField(default='Online', max_length=50),
        ),
    ]
