# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-12-26 09:07
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_auto_20171226_1657'),
    ]

    operations = [
        migrations.AddField(
            model_name='student_honorwall',
            name='student_total_number',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='student_honorwall',
            name='student_total_rank',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='student_honorwall',
            name='student_total_score',
            field=models.IntegerField(null=True),
        ),
    ]
