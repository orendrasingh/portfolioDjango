# Generated by Django 3.2.3 on 2021-05-24 11:14

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('portfolioapp', '0018_auto_20210524_1607'),
    ]

    operations = [
        migrations.AlterField(
            model_name='education',
            name='shortDescription',
            field=ckeditor.fields.RichTextField(max_length=250, null=True),
        ),
        migrations.AlterField(
            model_name='experience',
            name='shortDescription',
            field=ckeditor.fields.RichTextField(max_length=250, null=True),
        ),
    ]
