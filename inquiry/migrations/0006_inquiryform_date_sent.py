# Generated by Django 5.0.3 on 2024-05-14 17:35

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inquiry', '0005_remove_inquiryform_date_sent_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='inquiryform',
            name='date_sent',
            field=models.DateField(default=django.utils.timezone.now),
        ),
    ]