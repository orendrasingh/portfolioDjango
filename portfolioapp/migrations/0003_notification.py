# Generated by Django 3.2.3 on 2021-05-22 23:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolioapp', '0002_auto_20210523_0503'),
    ]

    operations = [
        migrations.CreateModel(
            name='notification',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('enabled', models.BooleanField(default=False)),
            ],
        ),
    ]
