# Generated by Django 4.1.5 on 2023-01-13 05:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('medical_reports', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='medicalreport',
            name='doctor',
        ),
    ]