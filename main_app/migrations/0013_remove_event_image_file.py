# Generated by Django 3.0.6 on 2020-05-09 22:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0012_remove_event_image_url'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='event',
            name='image_file',
        ),
    ]
