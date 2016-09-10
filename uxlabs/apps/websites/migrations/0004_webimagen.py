# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-09-10 18:03
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('websites', '0003_auto_20160910_1609'),
    ]

    operations = [
        migrations.CreateModel(
            name='WebImagen',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=64, verbose_name='Título')),
                ('imagen', models.ImageField(upload_to='galeria', verbose_name='Imagen')),
                ('web', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='galeria', to='websites.Web')),
            ],
            options={
                'verbose_name': 'Imagen',
                'verbose_name_plural': 'Galería',
            },
        ),
    ]
