# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-02-13 11:09
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('project_name', models.CharField(max_length=18)),
                ('slug', models.SlugField(primary_key=True, serialize=False)),
                ('short_description', models.CharField(max_length=110)),
                ('is_active', models.BooleanField()),
            ],
            options={
                'ordering': ('project_name',),
                'db_table': 'projects',
            },
        ),
        migrations.CreateModel(
            name='Release',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('release_name', models.CharField(max_length=18)),
                ('slug', models.SlugField(max_length=255)),
                ('release_date', models.DateTimeField(default=datetime.datetime.today)),
                ('body', models.TextField(help_text='Release description', max_length=2048)),
                ('is_active', models.BooleanField()),
                ('allow_comments', models.BooleanField(default=True)),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='projects.Project')),
            ],
            options={
                'ordering': ('project', 'release_name'),
                'db_table': 'releases',
            },
        ),
        migrations.AlterUniqueTogether(
            name='release',
            unique_together=set([('project', 'slug')]),
        ),
    ]
