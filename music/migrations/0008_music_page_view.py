# Generated by Django 3.2.9 on 2022-03-15 13:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('music', '0007_remove_music_song_online_url'),
    ]

    operations = [
        migrations.AddField(
            model_name='music',
            name='page_view',
            field=models.IntegerField(default=0),
        ),
    ]
