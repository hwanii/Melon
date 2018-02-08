# Generated by Django 2.0.2 on 2018-02-08 02:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('album', '0002_auto_20180207_1225'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='album',
            name='agency',
        ),
        migrations.RemoveField(
            model_name='album',
            name='genre',
        ),
        migrations.RemoveField(
            model_name='album',
            name='publisher',
        ),
        migrations.AddField(
            model_name='album',
            name='img_cover',
            field=models.ImageField(blank=True, upload_to='album', verbose_name='커버 이미지'),
        ),
    ]
