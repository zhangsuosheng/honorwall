# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-12-26 09:49
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0004_auto_20171226_1707'),
    ]

    operations = [
        migrations.AlterField(
            model_name='honor_competition',
            name='competition_type',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='home.Competition_type'),
        ),
        migrations.AlterField(
            model_name='honor_experience',
            name='competition_type',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='home.Competition_type'),
        ),
        migrations.AlterField(
            model_name='honor_paper_magazine',
            name='competition_type',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='home.Competition_type'),
        ),
        migrations.AlterField(
            model_name='honor_paper_meeting',
            name='competition_type',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='home.Competition_type'),
        ),
        migrations.AlterField(
            model_name='honor_patent',
            name='competition_type',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='home.Competition_type'),
        ),
        migrations.AlterField(
            model_name='honor_scholarship',
            name='competition_type',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='home.Competition_type'),
        ),
    ]
