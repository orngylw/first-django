# Generated by Django 3.2.13 on 2022-08-12 00:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tags', '0002_tag_color'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tag',
            name='color',
            field=models.CharField(choices=[('black', 'Black'), ('dark', 'Dark'), ('light', 'Light'), ('white', 'White'), ('primary', 'Primary'), ('link', 'Link'), ('info', 'Info'), ('success', 'Success'), ('warning', 'Warning'), ('danger', 'Danger')], default='primary', max_length=10),
        ),
    ]
