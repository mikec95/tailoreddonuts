# Generated by Django 4.2.2 on 2024-05-15 02:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gallery', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='galleryimage',
            name='image',
            field=models.ImageField(default='images/default-image.png', upload_to='gallery/images'),
        ),
    ]
