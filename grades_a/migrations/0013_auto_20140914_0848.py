# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('grades_a', '0012_auto_20140914_0846'),
    ]

    operations = [
        migrations.CreateModel(
            name='grades',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('alg_grade', models.IntegerField(default=1)),
                ('alg_term', models.IntegerField(default=-1)),
                ('geom_term', models.IntegerField(default=-1)),
                ('student_g', models.ForeignKey(to='grades_a.int_grades')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.RenameField(
            model_name='int_grades',
            old_name='alg_kr_grades',
            new_name='alg_grade',
        ),
        migrations.RemoveField(
            model_name='int_grades',
            name='alg_n_grades',
        ),
        migrations.RemoveField(
            model_name='int_grades',
            name='alg_sr_grades',
        ),
        migrations.RemoveField(
            model_name='int_grades',
            name='geom_kr_grades',
        ),
        migrations.RemoveField(
            model_name='int_grades',
            name='geom_n_grades',
        ),
        migrations.RemoveField(
            model_name='int_grades',
            name='geom_sr_grades',
        ),
        migrations.AlterField(
            model_name='int_grades',
            name='student',
            field=models.ForeignKey(to='grades_a.student'),
        ),
    ]
