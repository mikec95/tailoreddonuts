# Generated by Django 4.2.2 on 2024-04-08 23:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0006_product_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.ImageField(default='images/default-image.png', upload_to='images/'),
        ),
    ]
