# Generated by Django 3.2.6 on 2023-01-11 09:48

from django.db import migrations, models
import django_mysql.models


class Migration(migrations.Migration):

    dependencies = [
        ('healthcareApp', '0052_auto_20230111_1439'),
    ]

    operations = [
        migrations.AlterField(
            model_name='doctorinfo',
            name='visitingHours',
            field=django_mysql.models.ListCharField(models.CharField(blank=True, max_length=100, null=True), max_length=2200, null=True, size=20),
        ),
    ]