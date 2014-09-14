# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('grades_a', '0015_auto_20140914_0909'),
    ]

    operations = [
        migrations.CreateModel(
            name='lates_work',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('latest_grade', models.CharField(default=b'---', max_length=25)),
                ('name', models.OneToOneField(to='grades_a.student')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AlterField(
            model_name='student',
            name='alg_grades',
            field=models.TextField(default=True, max_length=500),
        ),
        migrations.AlterField(
            model_name='student',
            name='geom_grades',
            field=models.TextField(default=True, max_length=500),
        ),
    ]
