# Generated by Django 4.2.1 on 2023-05-16 14:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shared_rooms', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sharedroom',
            name='max_members',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='sharedroom',
            name='password',
            field=models.CharField(blank=True, max_length=8, null=True),
        ),
    ]
