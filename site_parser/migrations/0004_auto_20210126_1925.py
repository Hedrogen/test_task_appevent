# Generated by Django 3.1.5 on 2021-01-26 19:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('site_parser', '0003_auto_20210126_1748'),
    ]

    operations = [
        migrations.RenameField(
            model_name='article',
            old_name='time',
            new_name='created',
        ),
    ]
