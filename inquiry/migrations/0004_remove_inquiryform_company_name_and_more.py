# Generated by Django 5.0.3 on 2024-05-14 17:19

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inquiry', '0003_alter_inquiryform_company_name_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='inquiryform',
            name='company_name',
        ),
        migrations.RemoveField(
            model_name='inquiryform',
            name='delivery_address',
        ),
        migrations.RemoveField(
            model_name='inquiryform',
            name='delivery_date',
        ),
        migrations.RemoveField(
            model_name='inquiryform',
            name='event_date',
        ),
        migrations.RemoveField(
            model_name='inquiryform',
            name='event_type',
        ),
        migrations.RemoveField(
            model_name='inquiryform',
            name='num_guests',
        ),
        migrations.RemoveField(
            model_name='inquiryform',
            name='pickup_date',
        ),
        migrations.RemoveField(
            model_name='inquiryform',
            name='pickup_delivery',
        ),
        migrations.RemoveField(
            model_name='inquiryform',
            name='pickup_name',
        ),
        migrations.RemoveField(
            model_name='inquiryform',
            name='preferred_contact_time',
        ),
        migrations.AddField(
            model_name='inquiryform',
            name='date_sent',
            field=models.DateField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name='inquiryform',
            name='email',
            field=models.EmailField(default='xxx@mail.com', max_length=254),
        ),
        migrations.AddField(
            model_name='inquiryform',
            name='time_sent',
            field=models.TimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
