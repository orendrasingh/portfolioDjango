# Generated by Django 3.2.3 on 2021-05-23 10:06

from django.db import migrations, models
import portfolioapp.models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolioapp', '0005_about'),
    ]

    operations = [
        migrations.AddField(
            model_name='about',
            name='logo',
            field=models.ImageField(null=True, upload_to=portfolioapp.models.photo_path),
        ),
    ]
