# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2018-04-16 12:16
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('medicines', '0008_specification'),
    ]

    operations = [
        migrations.AlterField(
            model_name='medicine',
            name='med_logo',
            field=models.FileField(upload_to=''),
        ),
        migrations.AlterField(
            model_name='products',
            name='product_logo',
            field=models.FileField(upload_to=''),
        ),
    ]
