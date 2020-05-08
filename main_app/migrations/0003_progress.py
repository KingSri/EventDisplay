# Generated by Django 3.0.5 on 2020-05-08 06:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0002_event_user'),
    ]

    operations = [
        migrations.CreateModel(
            name='Progress',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(choices=[('N', 'Not Yet Started'), ('I', 'In Progress'), ('C', 'Completed')], default=0, max_length=1)),
                ('event', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main_app.Event')),
            ],
        ),
    ]
