# Generated by Django 3.1.1 on 2020-10-29 11:25

import ckeditor_uploader.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0007_auto_20201029_1119'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='manuale',
            name='file',
        ),
        migrations.AlterField(
            model_name='manuale',
            name='title',
            field=ckeditor_uploader.fields.RichTextUploadingField(),
        ),
    ]
