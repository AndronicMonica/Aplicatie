# Generated by Django 2.0.5 on 2018-05-18 15:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0004_imprumuturi_titlul_cartii'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='imprumuturi',
            name='titlul_cartii',
        ),
    ]
