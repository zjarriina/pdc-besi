# Generated by Django 3.1.1 on 2020-10-29 14:55

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0012_auto_20201029_1217'),
    ]

    operations = [
        migrations.AddField(
            model_name='manuale',
            name='po',
            field=models.TextField(default=datetime.datetime(2020, 10, 29, 14, 55, 31, 103099, tzinfo=utc)),
            preserve_default=False,
        ),
    ]
