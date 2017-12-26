# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-12-26 09:55
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0006_auto_20171226_1752'),
    ]

    operations = [
        migrations.AlterField(
            model_name='honor_competition',
            name='honor_competition_check_time',
            field=models.DateTimeField(null=True),
        ),
        migrations.AlterField(
            model_name='honor_experience',
            name='honor_experience_check_time',
            field=models.DateTimeField(null=True),
        ),
        migrations.AlterField(
            model_name='honor_paper_magazine',
            name='honor_paper_magazine_check_time',
            field=models.DateTimeField(null=True),
        ),
        migrations.AlterField(
            model_name='honor_paper_meeting',
            name='honor_paper_meeting_check_time',
            field=models.DateTimeField(null=True),
        ),
        migrations.AlterField(
            model_name='honor_patent',
            name='honor_patent_check_time',
            field=models.DateTimeField(null=True),
        ),
        migrations.AlterField(
            model_name='honor_scholarship',
            name='honor_scholarship_check_time',
            field=models.DateTimeField(null=True),
        ),
    ]