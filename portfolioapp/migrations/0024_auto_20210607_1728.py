# Generated by Django 3.2.3 on 2021-06-07 11:58

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('portfolioapp', '0023_auto_20210607_1520'),
    ]

    operations = [
        migrations.AlterField(
            model_name='education',
            name='description',
            field=ckeditor.fields.RichTextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='experience',
            name='description',
            field=ckeditor.fields.RichTextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='personalprojects',
            name='description',
            field=ckeditor.fields.RichTextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='recentwork',
            name='description',
            field=ckeditor.fields.RichTextField(blank=True, null=True),
        ),
    ]