# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-10-08 23:35
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contacts', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contacto',
            name='estado',
            field=models.CharField(choices=[('P', 'Pendiente'), ('A', 'Atentido')], default='P', max_length=1, verbose_name='Estado'),
        ),
    ]
