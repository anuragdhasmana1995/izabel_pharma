# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2018-04-11 11:23
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('medicines', '0004_auto_20180410_1449'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='specification',
            name='specification',
        ),
        migrations.AddField(
            model_name='medicine',
            name='specification',
            field=models.ManyToManyField(default='NA', to='medicines.Specification'),
        ),
    ]