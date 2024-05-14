# Generated by Django 5.0.3 on 2024-05-14 19:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inquiry', '0007_inquiryform_time_sent'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='inquiryform',
            name='date_sent',
        ),
        migrations.RemoveField(
            model_name='inquiryform',
            name='email',
        ),
        migrations.RemoveField(
            model_name='inquiryform',
            name='time_sent',
        ),
        migrations.AlterField(
            model_name='inquiryform',
            name='phone_number',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
    ]