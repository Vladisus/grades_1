# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('grades_a', '0009_auto_20140913_2042'),
    ]

    operations = [
        migrations.CreateModel(
            name='int_grades',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('alg_n_grades', models.IntegerField(default=1)),
                ('alg_sr_grades', models.IntegerField(default=1)),
                ('alg_kr_grades', models.IntegerField(default=1)),
                ('geom_n_grades', models.IntegerField(default=1)),
                ('geom_sr_grades', models.IntegerField(default=1)),
                ('geom_kr_grades', models.IntegerField(default=1)),
                ('alg_term', models.IntegerField(default=-1)),
                ('student', models.OneToOneField(to='grades_a.student')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
