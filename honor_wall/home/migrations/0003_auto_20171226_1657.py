# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-12-26 08:57
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_links'),
    ]

    operations = [
        migrations.AddField(
            model_name='student_honorwall',
            name='student_competition_rank',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='student_honorwall',
            name='student_experience_rank',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='student_honorwall',
            name='student_paper_magazine_rank',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='student_honorwall',
            name='student_paper_meeting_rank',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='student_honorwall',
            name='student_paper_rank',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='student_honorwall',
            name='student_patent_rank',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='student_honorwall',
            name='student_scholarship_rank',
            field=models.IntegerField(null=True),
        ),
    ]
