# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-04-24 20:34
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('study', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='number',
            field=models.IntegerField(default=6301112222),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='checkedin',
            name='people',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='selectedStudent', to='study.Student'),
        ),
    ]