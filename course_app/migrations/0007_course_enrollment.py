# Generated by Django 4.1.4 on 2022-12-11 10:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('course_app', '0006_rename_module_video_module'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='enrollment',
            field=models.BooleanField(default=False),
        ),
    ]
