# Generated by Django 3.0.6 on 2020-05-10 18:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0015_event_photo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='photo',
            field=models.ImageField(blank=True, default='default.jpg', upload_to=''),
        ),
    ]
