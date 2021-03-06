# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-12-01 10:36
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student_honorwall',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('student_competition_number', models.IntegerField()),
                ('student_competition_score', models.IntegerField()),
                ('student_paper_number', models.IntegerField()),
                ('student_paper_score', models.IntegerField()),
                ('student_paper_magazine_number', models.IntegerField()),
                ('student_paper_magazine_score', models.IntegerField()),
                ('student_paper_meeting_number', models.IntegerField()),
                ('student_paper_meeting_score', models.IntegerField()),
                ('student_patent_number', models.IntegerField()),
                ('student_patent_score', models.IntegerField()),
                ('student_scholarship_number', models.IntegerField()),
                ('student_scholarship_score', models.IntegerField()),
                ('student_experience_number', models.IntegerField()),
                ('student_experience_score', models.IntegerField()),
                ('student_portrait', models.ImageField(upload_to='')),
            ],
        ),
        migrations.CreateModel(
            name='Student_message_editable',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('student_nickname', models.CharField(default='无', max_length=20)),
                ('student_birthday', models.CharField(max_length=20)),
                ('student_political_state', models.CharField(max_length=20)),
                ('student_people', models.CharField(max_length=10)),
                ('student_birthplace', models.CharField(max_length=20)),
                ('student_document_type', models.CharField(max_length=10)),
                ('student_document_number', models.CharField(max_length=100)),
                ('student_email', models.EmailField(max_length=30, unique=True)),
                ('student_phone_number', models.IntegerField(unique=True)),
                ('student_qq_number', models.IntegerField(unique=True)),
                ('student_photo', models.ImageField(upload_to='img')),
                ('student_name_conceal', models.BooleanField(default=False)),
                ('student_contact_conceal', models.BooleanField(default=False)),
                ('student_sex_conceal', models.BooleanField(default=False)),
                ('student_all_conceal', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Student_message_uneditable',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('student_name', models.CharField(max_length=30)),
                ('student_sex', models.BooleanField()),
                ('student_id', models.IntegerField(unique=True)),
                ('student_field', models.CharField(max_length=20)),
                ('student_classname', models.CharField(max_length=10)),
                ('student_faculty', models.CharField(max_length=20)),
                ('student_grade', models.IntegerField()),
                ('student_state', models.BooleanField()),
            ],
        ),
        migrations.AddField(
            model_name='student_message_editable',
            name='student',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home_student.Student_message_uneditable', to_field='student_id'),
        ),
        migrations.AddField(
            model_name='student_honorwall',
            name='student',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home_student.Student_message_uneditable', to_field='student_id'),
        ),
    ]
