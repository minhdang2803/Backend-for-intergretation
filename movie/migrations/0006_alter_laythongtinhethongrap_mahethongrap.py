# Generated by Django 3.2.9 on 2021-11-07 15:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movie', '0005_rename_quanlyhethongrap_laythongtinhethongrap'),
    ]

    operations = [
        migrations.AlterField(
            model_name='laythongtinhethongrap',
            name='maHeThongRap',
            field=models.CharField(max_length=50, primary_key=True, serialize=False),
        ),
    ]