# Generated by Django 4.2.2 on 2024-04-02 03:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_alter_product_item_title'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='slug',
            field=models.SlugField(
                editable=False, help_text='Unique slug for URL', unique=True),
        ),
    ]
