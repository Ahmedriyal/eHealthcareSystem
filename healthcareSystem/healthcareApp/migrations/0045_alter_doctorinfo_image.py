# Generated by Django 3.2.6 on 2022-02-15 11:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('healthcareApp', '0044_alter_doctorinfo_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='doctorinfo',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='doctorsPP'),
        ),
    ]
