# Generated by Django 5.0.1 on 2024-03-17 15:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('med_app', '0009_rename_name_appointment_pt_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contactus',
            name='phone',
            field=models.CharField(max_length=15),
        ),
    ]
