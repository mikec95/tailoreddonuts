# Generated by Django 4.2.2 on 2024-05-15 02:31

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='GalleryImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image_title', models.CharField(help_text='Image Title', max_length=250)),
                ('description', models.TextField(blank=True, default='', help_text='Description of the product')),
                ('image', models.ImageField(default='images/default-image.png', upload_to='images/')),
                ('slug', models.SlugField(help_text='Unique slug for URL', unique=True)),
            ],
            options={
                'verbose_name_plural': 'Gallery Images',
            },
        ),
    ]
