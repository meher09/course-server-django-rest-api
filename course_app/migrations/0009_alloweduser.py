# Generated by Django 4.1.4 on 2022-12-24 15:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('course_app', '0008_teammember'),
    ]

    operations = [
        migrations.CreateModel(
            name='AllowedUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.CharField(max_length=255, unique=True)),
                ('facebook_id', models.CharField(max_length=255, unique=True)),
            ],
        ),
    ]