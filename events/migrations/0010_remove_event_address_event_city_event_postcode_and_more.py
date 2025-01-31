# Generated by Django 4.2.18 on 2025-01-26 17:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0009_alter_event_organizer'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='event',
            name='address',
        ),
        migrations.AddField(
            model_name='event',
            name='city',
            field=models.CharField(default='default', max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='event',
            name='postcode',
            field=models.CharField(default='default', max_length=20),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='event',
            name='street',
            field=models.CharField(default='default', max_length=200),
            preserve_default=False,
        ),
    ]
