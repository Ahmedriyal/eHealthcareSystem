# Generated by Django 3.2.6 on 2021-08-07 04:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('healthcareApp', '0004_alter_usertype_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='doctorinfo',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='doctorinfo',
            name='fees',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
