# Generated by Django 3.2.13 on 2022-08-10 00:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tags', '0001_initial'),
        ('praises', '0013_auto_20220809_1958'),
    ]

    operations = [
        migrations.AddField(
            model_name='praise',
            name='tags',
            field=models.ManyToManyField(to='tags.Tag'),
        ),
    ]
