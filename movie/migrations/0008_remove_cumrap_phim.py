# Generated by Django 3.2.8 on 2021-11-20 02:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('movie', '0007_auto_20211120_0947'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cumrap',
            name='phim',
        ),
    ]
