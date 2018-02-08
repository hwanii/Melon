# Generated by Django 2.0.2 on 2018-02-07 03:03

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('artist', '0002_auto_20180206_1655'),
    ]

    operations = [
        migrations.CreateModel(
            name='Album',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('album_name', models.CharField(max_length=50, verbose_name='앨범명')),
                ('release_date', models.DateField(verbose_name='발매일')),
                ('genre', models.CharField(max_length=50, verbose_name='장르')),
                ('agency', models.CharField(blank=True, max_length=50, verbose_name='기획사')),
                ('publisher', models.CharField(blank=True, max_length=50, verbose_name='발매사')),
                ('album_intro', models.TextField(blank=True, verbose_name='소개')),
                ('artist', models.ManyToManyField(to='artist.Artist')),
            ],
        ),
    ]
