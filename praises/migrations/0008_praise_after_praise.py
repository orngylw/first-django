# Generated by Django 3.2.12 on 2022-06-06 18:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('praises', '0007_alter_praise_img_path'),
    ]

    operations = [
        migrations.AddField(
            model_name='praise',
            name='after_praise',
            field=models.CharField(blank=True, choices=[('헌금찬양', '헌금찬양')], max_length=5),
        ),
    ]