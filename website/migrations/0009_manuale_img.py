# Generated by Django 3.1.1 on 2020-10-29 12:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0008_auto_20201029_1125'),
    ]

    operations = [
        migrations.AddField(
            model_name='manuale',
            name='img',
            field=models.ImageField(blank=True, null=True, upload_to='media/'),
        ),
    ]