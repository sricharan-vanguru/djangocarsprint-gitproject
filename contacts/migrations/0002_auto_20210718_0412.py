# Generated by Django 3.1.1 on 2021-07-17 22:42

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contacts', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='contact',
            name='created_data',
        ),
        migrations.AddField(
            model_name='contact',
            name='created_date',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 7, 18, 4, 12, 8, 504613)),
        ),
    ]
