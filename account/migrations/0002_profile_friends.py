# Generated by Django 4.2.6 on 2024-01-28 15:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='friends',
            field=models.IntegerField(default=0),
        ),
    ]
