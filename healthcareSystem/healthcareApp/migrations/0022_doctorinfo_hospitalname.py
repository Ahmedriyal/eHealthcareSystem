# Generated by Django 3.2.6 on 2021-08-11 17:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('healthcareApp', '0021_auto_20210811_2256'),
    ]

    operations = [
        migrations.AddField(
            model_name='doctorinfo',
            name='hospitalName',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]