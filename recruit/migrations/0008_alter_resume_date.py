# Generated by Django 3.2.3 on 2022-09-07 08:16

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('recruit', '0007_resume'),
    ]

    operations = [
        migrations.AlterField(
            model_name='resume',
            name='date',
            field=models.DateField(default=datetime.datetime(2022, 9, 7, 8, 16, 58, 671963, tzinfo=utc)),
        ),
    ]
