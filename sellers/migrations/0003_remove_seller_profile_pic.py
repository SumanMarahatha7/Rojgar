# Generated by Django 3.0.6 on 2020-06-02 11:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sellers', '0002_auto_20200601_2116'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='seller',
            name='profile_pic',
        ),
    ]
