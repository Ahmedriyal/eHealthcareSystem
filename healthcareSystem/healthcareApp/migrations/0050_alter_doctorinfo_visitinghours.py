# Generated by Django 3.2.6 on 2023-01-10 04:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('healthcareApp', '0049_alter_doctorinfo_visitinghours'),
    ]

    operations = [
        migrations.AlterField(
            model_name='doctorinfo',
            name='visitingHours',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
    ]
