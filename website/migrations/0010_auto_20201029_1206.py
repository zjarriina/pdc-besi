# Generated by Django 3.1.1 on 2020-10-29 12:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0009_manuale_img'),
    ]

    operations = [
        migrations.AlterField(
            model_name='manuale',
            name='img',
            field=models.FileField(blank=True, null=True, upload_to='media/'),
        ),
    ]
