# Generated by Django 3.1.1 on 2020-10-29 11:19

import ckeditor_uploader.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0006_auto_20201028_1211'),
    ]

    operations = [
        migrations.AlterField(
            model_name='manuale',
            name='file',
            field=ckeditor_uploader.fields.RichTextUploadingField(),
        ),
    ]
