# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2018-04-15 17:41
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('medicines', '0006_auto_20180415_2300'),
    ]

    operations = [
        migrations.AlterField(
            model_name='medicine',
            name='manufacturer',
            field=models.CharField(max_length=250),
        ),
    ]
