# Generated by Django 3.2.6 on 2021-08-13 18:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('healthcareApp', '0027_auto_20210813_1150'),
    ]

    operations = [
        migrations.AlterField(
            model_name='doctorinfo',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='doctorsPP/'),
        ),
    ]
