# Generated by Django 2.0.5 on 2018-05-18 14:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0002_auto_20180518_1750'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='imprumuturi',
            name='titlu_carte',
        ),
    ]