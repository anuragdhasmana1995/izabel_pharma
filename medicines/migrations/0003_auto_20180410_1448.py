# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2018-04-10 09:18
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('medicines', '0002_auto_20180410_1434'),
    ]

    operations = [
        migrations.AlterField(
            model_name='specification',
            name='salts',
            field=models.TextField(max_length=250),
        ),
        migrations.AlterField(
            model_name='specification',
            name='salts_quantity',
            field=models.TextField(max_length=100),
        ),
    ]
