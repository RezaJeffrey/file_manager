# Generated by Django 4.1.4 on 2022-12-31 19:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='created_time',
        ),
        migrations.RemoveField(
            model_name='user',
            name='updated_time',
        ),
    ]
