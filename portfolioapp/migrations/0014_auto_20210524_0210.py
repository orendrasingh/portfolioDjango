# Generated by Django 3.2.3 on 2021-05-23 20:40

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolioapp', '0013_alter_technology2_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='notification',
            name='msg',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='recentwork',
            name='description',
            field=ckeditor.fields.RichTextField(),
        ),
    ]
