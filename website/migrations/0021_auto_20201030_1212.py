# Generated by Django 3.1.1 on 2020-10-30 12:12

import ckeditor_uploader.fields
from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0020_auto_20201030_1211'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='testzone',
            name='url',
        ),
        migrations.AddField(
            model_name='testzone',
            name='link',
            field=ckeditor_uploader.fields.RichTextUploadingField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='testzone',
            name='title',
            field=models.TextField(),
        ),
    ]