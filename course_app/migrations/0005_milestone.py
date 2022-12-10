# Generated by Django 4.1.4 on 2022-12-10 09:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('course_app', '0004_course_price'),
    ]

    operations = [
        migrations.CreateModel(
            name='Milestone',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='Course Name')),
                ('slug', models.SlugField(blank=True, null=True, unique=True)),
                ('description', models.TextField(blank=True, max_length=500, null=True)),
            ],
        ),
    ]