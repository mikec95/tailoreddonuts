# Generated by Django 4.2.2 on 2024-05-17 01:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gallery', '0002_alter_galleryimage_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='galleryimage',
            name='slug',
        ),
    ]
