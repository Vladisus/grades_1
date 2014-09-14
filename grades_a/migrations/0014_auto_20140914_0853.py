# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('grades_a', '0013_auto_20140914_0848'),
    ]

    operations = [
        migrations.RenameField(
            model_name='grades',
            old_name='student_g',
            new_name='student',
        ),
        migrations.RemoveField(
            model_name='int_grades',
            name='alg_grade',
        ),
        migrations.RemoveField(
            model_name='int_grades',
            name='alg_term',
        ),
        migrations.RemoveField(
            model_name='int_grades',
            name='geom_term',
        ),
        migrations.AddField(
            model_name='grades',
            name='geom_grade',
            field=models.IntegerField(default=1),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='int_grades',
            name='student',
            field=models.ForeignKey(to='grades_a.student'),
        ),
    ]
