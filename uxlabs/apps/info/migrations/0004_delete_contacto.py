# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-10-02 17:57
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('info', '0003_contacto'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Contacto',
        ),
    ]