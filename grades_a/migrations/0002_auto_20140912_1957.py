# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('grades_a', '0001_initial'),
    ]

    operations = [
        migrations.DeleteModel(
            name='User_model',
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.TextField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Grades',
            fields=[
                ('student', models.OneToOneField(primary_key=True, serialize=False, to='grades_a.Student')),
                ('grade', models.IntegerField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
