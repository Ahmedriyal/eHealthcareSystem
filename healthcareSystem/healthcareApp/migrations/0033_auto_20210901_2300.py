# Generated by Django 3.2.6 on 2021-09-01 17:00

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('healthcareApp', '0032_auto_20210901_2127'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='appointment',
            name='appointment_list',
        ),
        migrations.AddField(
            model_name='appointment',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.DeleteModel(
            name='Appointment_list',
        ),
    ]
